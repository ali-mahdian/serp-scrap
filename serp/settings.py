# Scrapy settings for serp project

BOT_NAME = 'serp'

SPIDER_MODULES = ['serp.spiders']
NEWSPIDER_MODULE = 'serp.spiders'

# DEPTH SETTINGS (how many pages you want to go deeper for crawling)
DEPTH_LIMIT = 1

# identify the user-agent (update to latest mozilla for ubuntu)
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0'

# Obey robots.txt rules (sorry!! google doesn't allow!)
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy
CONCURRENT_REQUESTS = 5

# Configure a delay for requests for the same website
DOWNLOAD_DELAY = 10

CONCURRENT_REQUESTS_PER_DOMAIN = 5
CONCURRENT_REQUESTS_PER_IP = 4

# Configure item pipelines (should be a dict)
ITEM_PIPELINES = {
    'serp.pipelines.ExcelExporter': 100,
}

# Enable and configure the AutoThrottle extension
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 2.5
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = True

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'serp.middlewares.SerpSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html

# DOWNLOADER_MIDDLEWARES = {
    # 'serp.middlewares.SerpDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

