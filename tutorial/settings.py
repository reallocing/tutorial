# -*- coding: utf-8 -*-
#encoding=utf-8
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')
# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'

DATABASE = {'drivername': 'mysql',
            'username': 'root',
            'password': '123456',
            'database': 'security'
            }

# DATABASE = {
    # 'host': 'localhost',
    # 'user': 'root',
    # 'password': '123456',
    # 'db':'security',
    # 'charset':'utf8'
# }

ITEM_PIPELINES = {
    'tutorial.pipelines.TutorialPipeline':300
}

#ITEM_PIPELINES = {'tutorial.pipelines.MySQLStorePipeline':300}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
