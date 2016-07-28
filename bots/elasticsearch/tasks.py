import logging
import re

from django.apps import apps
from elasticsearch import helpers
from elasticsearch import Elasticsearch

from project import settings

from share.tasks import ProviderTask
from share.models import AbstractCreativeWork
from share.models import Entity
from share.models import Person
from share.models import Tag

logger = logging.getLogger(__name__)


def safe_substr(value, length=32000):
    if value:
        return str(value)[:length]
    return None

def add_suggest(obj, input, payload_keys):
    word_starts = re.finditer(r'\b\w', input)
    obj['suggest'] = {
        'input': [ input[m.start():] for m in word_starts ],
        'payload': { k: obj[k] for k in payload_keys }
    }
    return obj

class IndexModelTask(ProviderTask):

    def do_run(self, model_name, ids):
        es_client = Elasticsearch(settings.ELASTICSEARCH_URL)
        model = apps.get_model('share', model_name)
        for resp in helpers.streaming_bulk(es_client, self.bulk_stream(model, ids)):
            logger.debug(resp)

    def bulk_stream(self, model, ids):
        opts = {'_index': settings.ELASTICSEARCH_INDEX, '_type': model.__name__.lower()}
        qs = model.objects.filter(id__in=ids)
        for inst in qs.all():
            # if inst.is_delete:  # TODO
            #     yield {'_id': inst.pk, '_op_type': 'delete', **opts}
            yield {'_id': inst.pk, '_op_type': 'index', **self.serialize(inst), **opts}

    def serialize(self, inst):
        return {
            AbstractCreativeWork: self.serialize_creative_work,
            Entity: self.serialize_entity,
            Person: self.serialize_person,
            Tag: self.serialize_tag,
        }[type(inst)._meta.concrete_model](inst)

    def serialize_person(self, person, suggest=True):
        serialized_person = {
            '@id': person.pk,
            '@type': 'person',
            'suffix': safe_substr(person.suffix),
            'given_name': safe_substr(person.given_name),
            'family_name': safe_substr(person.family_name),
            'full_name': safe_substr(person.get_full_name()),
            'additional_name': safe_substr(person.additional_name),
            'identifiers': [{
                'url': identifier.url,
                'base_url': identifier.base_url,
            } for identifier in person.identifiers.all()],
            'affiliations': [
                self.serialize_entity(affiliation, False)
                for affiliation in
                person.affiliations.all()
            ],
            'sources': [source.robot for source in person.sources.all()],
        }
        if suggest:
            return add_suggest(serialized_person,
                               input=serialized_person['full_name'],
                               payload_keys=('@id', '@type', 'full_name'))
        else:
            return serialized_person

    def serialize_person_link(self, person):
        return {
            '@id': person.pk,
            '@type': 'person',
            'name': safe_substr(entity.name),
        }


    def serialize_entity(self, entity, suggest=True):
        serialized_entity = {
            '@id': entity.pk,
            '@type': type(entity).__name__.lower(),
            'name': safe_substr(entity.name),
            'url': entity.url,
            'location': safe_substr(entity.location),
        }
        if suggest:
            return add_suggest(serialized_entity,
                               input = serialized_entity['name'],
                               payload_keys = ('@id', '@type', 'name'))
        else:
            return serialized_entity

    def serialize_tag(self, tag):
        serialized_tag = {
            '@id': str(tag.pk),
            '@type': 'tag',
            'name': safe_substr(tag.name),
        }
        return add_suggest(serialized_tag,
                           input = serialized_tag['name'],
                           payload_keys = ('@id', 'name'))

    def serialize_creative_work(self, creative_work):
        return {
            '@type': type(creative_work).__name__.lower(),
            'associations': [
                self.serialize_entity(association, False)
                for association in [
                    *creative_work.funders.all(),
                    *creative_work.publishers.all(),
                    *creative_work.institutions.all(),
                    *creative_work.organizations.all()
                ]
            ],
            'title': safe_substr(creative_work.title),
            'language': safe_substr(creative_work.language),
            'subject': safe_substr(creative_work.subject),
            'description': safe_substr(creative_work.description),
            'date': (
                creative_work.date_published or creative_work.date_updated or creative_work.date_created
            ).isoformat(),
            'date_created': creative_work.date_created.isoformat(),
            'date_modified': creative_work.date_modified.isoformat(),
            'date_updated': creative_work.date_updated.isoformat() if creative_work.date_updated else None,
            'date_published': creative_work.date_published.isoformat() if creative_work.date_published else None,
            'tags': [safe_substr(tag) for tag in creative_work.tags.all()],
            'links': [safe_substr(link) for link in creative_work.links.all()],
            'awards': [safe_substr(award) for award in creative_work.awards.all()],
            'venues': [safe_substr(venue) for venue in creative_work.venues.all()],
            'sources': [source.robot for source in creative_work.sources.all()],
            'contributors': [self.serialize_person(person, False) for person in creative_work.contributors.all()],
        }

class IndexSourceTask(ProviderTask):

    def do_run(self):
        es_client = Elasticsearch(settings.ELASTICSEARCH_URL)
        for resp in helpers.streaming_bulk(es_client, self.bulk_stream()):
            logger.debug(resp)

    def bulk_stream(self):
        ShareUser = apps.get_model('share.ShareUser')
        opts = {'_index': settings.ELASTICSEARCH_INDEX, '_type': 'source'}
        for source in ShareUser.objects.exclude(robot='').exclude(long_title='').all():
            yield {'_op_type': 'index', '_id': source.robot, **self.serialize(source), **opts}

    def serialize(self, source):
        serialized_source = {
            '@id': str(source.pk),
            '@type': 'source',
            'long_name': safe_substr(source.long_title),
            'short_name': safe_substr(source.robot)
        }
        return add_suggest(serialized_source,
                           input = serialized_source['long_name'],
                           payload_keys = ('@id', '@type', 'long_name', 'short_name'))

