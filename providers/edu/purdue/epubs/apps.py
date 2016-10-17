from share.provider import OAIProviderAppConfig


class AppConfig(OAIProviderAppConfig):
    name = 'providers.edu.purdue.epubs'
    version = '0.0.1'
    title = 'purdue.epubs'
    long_title = 'Purdue e-Pubs'
    home_page = 'http://docs.lib.purdue.edu/'
    url = 'http://docs.lib.purdue.edu/do/oai/'
    approved_sets = [
        u'ddad2011',
        u'gully',
        u'gully_images',
        u'advancegsr',
        u'a3ir-core',
        u'alsnscort',
        u'atg',
        u'agroenviron',
        u'airties',
        u'aps',
        u'aqrr',
        u'techdepts',
        u'alsreports',
        u'artlas',
        u'atspmw',
        u'atpubs',
        u'atgrads',
        u'atugres',
        u'bio',
        u'biopre',
        u'biopub',
        u'bioinformaticspubs',
        u'nanoetd',
        u'nanofacility',
        u'nano',
        u'nanoposter',
        u'botrsrchctr',
        u'brc',
        u'comm',
        u'commpubs',
        u'cfshonors',
        u'cfstheses',
        u'clcweblibrary',
        u'clcweb',
        u'coolingpubs',
        u'cffamilies',
        u'cffpub',
        u'cie',
        u'cwc',
        u'charleston',
        u'claritas',
        u'cgg',
        u'ag',
        u'education',
        u'engr',
        u'hhs',
        u'hhshonors',
        u'hhstheses',
        u'hhsrci',
        u'cla',
        u'pharm',
        u'sci',
        u'tech',
        u'techdirproj',
        u'techdissertations',
        u'techmasters',
        u'techetds',
        u'vet',
        u'vetbooks',
        u'cgtpubs',
        u'cooling',
        u'cc',
        u'ccpubs',
        u'cctech',
        u'dlcpre',
        u'dlcpub',
        u'datacurationprofiles',
        u'dcp',
        u'dcpsymposium',
        u'dcptoolkit',
        u'dilcs',
        u'dilsymposium',
        u'dawnordoom',
        u'agrypubs',
        u'cpbpubs',
        u'agcomm',
        u'agecon',
        u'agedocs',
        u'agry',
        u'ansc',
        u'anscpubs',
        u'anscgrads',
        u'anth',
        u'anthpubs',
        u'ad',
        u'adpubs',
        u'avtech',
        u'atdp',
        u'attheses',
        u'bms',
        u'bmspubs',
        u'biochem',
        u'biochempubs',
        u'biosci',
        u'bioscipubs',
        u'btny',
        u'btnypubs',
        u'bcm',
        u'bcmdp',
        u'bcmtheses',
        u'bcm_pubs',
        u'chem',
        u'chempubs',
        u'cpb',
        u'cgt',
        u'cgttheses',
        u'cgtdp',
        u'cit',
        u'comp_sci',
        u'cspubs',
        u'cstech',
        u'citdp',
        u'cittheses',
        u'csr',
        u'csrpubs',
        u'edci',
        u'edcipubs',
        u'eas',
        u'easpubs',
        u'econ',
        u'econpubs',
        u'edst',
        u'edstpubs',
        u'ece',
        u'ecepubs',
        u'ecetheses',
        u'ecetr',
        u'ecet',
        u'engl',
        u'englpubs',
        u'entm',
        u'entmpubs',
        u'foodsci',
        u'foodscipubs', u'fnr', u'fnrpubs',
        u'hk', u'hkpubs', u'hist', u'histpubs', u'histwp', u'hlapubs', u'hla', u'htm', u'htmpubs', u'hdfspubs', u'hdfs',
        u'ipph', u'ipphpubs', u'mgmt', u'mgmtpubs', u'math', u'mathpubs', u'metdp', u'mettheses', u'mcmp', u'mcmppubs',
        u'mcmpgrads', u'fn', u'fnpubs', u'phpr', u'phprpubs', u'phil', u'philpubs', u'physics', u'physastrpubs',
        u'physics_articles', u'polisci', u'pspubs', u'psych', u'psychpubs', u'soc', u'socpubs', u'slhs', u'slhspubs',
        u'stat', u'statpubs', u'statgrads', u'tli', u'tlidp', u'tlitheses', u'theatre', u'theatrepubs', u'vcs',
        u'vcspubs', u'ydae', u'ydaepubs', u'dtrs', u'dlc', u'dp', u'cem', u'cempubs', u'dance', u'dancepubs', u'eee',
        u'eeepubs', u'music', u'musicpubs', u'drinet', u'ectfs', u'ectfs_archive', u'eandc', u'ect', u'soeslsummit',
        u'ebull', u'cit_articles', u'fosr', u'gisday', u'geopubs', u'ggrs', u'gpridocs', u'gtaptp', u'gtapwp',
        u'giftedchildren', u'gbl', u'gpri', u'gpripb', u'agext', u'anrhist', u'hivelab', u'hivepubs', u'hivepres',
        u'hivetechs', u'hees', u'honors', u'hon_stupubs', u'impactcms', u'impactpres', u'imp', u'impactpubs',
        u'impactreps', u'impsymposium', u'waterpubs', u'watertech', u'agroenviron_images', u'inltap',
        u'inltapdirectory', u'inltappubs', u'inltaptechs', u'imr', u'iwrrc', u'itap', u'impact', u'idc', u'idcpres',
        u'idcpubs', u'ijpbl', u'alsinternal', u'iatul2010', u'icec', u'thermal', u'icdcs', u'ihpbc', u'i3r2', u'iracc',
        u'jtrpaffdocs', u'jtrpdata', u'jtrpdocs', u'jtrppres', u'jtrpsuppm', u'jtrp', u'jtrprogram', u'jafe', u'jate',
        u'jca', u'jhpee', u'jpeer', u'jsaaea', u'jto', u'kran', u'lars_symp', u'larstech', u'lita2009', u'lars',
        u'lib_fscm', u'lib_fspres', u'lib_fsdocs', u'lib_fssup', u'librariespublishing', u'libreports', u'lib_research',
        u'lsg', u'civl', u'civeng', u'civlgradreports', u'cetheses', u'modvis', u'ngica_artcl', u'ngica_note', u'ovpr',
        u'provost', u'provost_pubs', u'ocs', u'ocspub', u'open_access_dissertations', u'open_access_theses',
        u'nanodocs', u'p12eders', u'pibergiim', u'pibergpres', u'pibergpubs', u'prism', u'vpa', u'paij', u'greenhouse',
        u'policiesforprogress', u'nasap', u'aseptic', u'iatul', u'herrick', u'alspub', u'ciberwp', u'fruitveg',
        u'fvtrials', u'purduegisday', u'piberg', u'pjsl', u'libraries', u'plas', u'pmag', u'pmcg', u'pmrg',
        u'p12nsummit', u'roadschool', u'thepress', u'purduepress_ebooks', u'pupoaj', u'pupsubj', u'presssupp',
        u'writinglab', u'writinglabsdrp', u'writinglabgradpres', u'writinglabgradpubs', u'writinglabpres',
        u'writinglabpubs', u'writinglabreps', u'writinglabetd', u'rche_pre', u'rche_pro', u'rche_rp', u'rche_rep',
        u'rche_wp', u'revisioning', u'rche', u'nasarp', u'sbrite', u'sbritereports', u'sps', u'spsoaj', u'sps_ebooks',
        u'sotl', u'aae', u'aaepubs', u'abe', u'abepubs', u'che', u'chepubs', u'ene', u'enepubs', u'enegs', u'enewp',
        u'et', u'etdp', u'ettheses', u'hsci', u'hscipubs', u'hscigradpubs', u'ie', u'iepubs', u'lc', u'lcpubs', u'lcwp',
        u'mse', u'msepubs', u'me', u'mepubs', u'ne', u'nepubs', u'nursing', u'nursingpubs', u'shofar', u'ses2014',
        u'sppp', u'demolition', u'agep', u'deansbible', u'passarowitz', u'reframit', u'swadin', u'nasatr', u'tlipubs',
        u'puhistorian', u'icpns', u'atsmw', u'jps', u'jpur', u'jpur_proposals', u'rueffgalleries', u'surf', u'etd',
        u'timber', u'transform', u'archives', u'gendes', u'ovprcores', u'demingconf', u'bme', u'bmepubs', u'bmegrads',
        u'swresources'
    ]