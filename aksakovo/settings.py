BOT_NAME = 'aksakovo'

SPIDER_MODULES = ['aksakovo.spiders']
NEWSPIDER_MODULE = 'aksakovo.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'aksakovo.pipelines.AksakovoPipeline': 100,

}