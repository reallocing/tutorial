# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item

#from sqlalchemy.orm import sessionmaker
#from models import Dmoz, db_connect, create_dmoz_table
#  
#class TutorialPipeline(object):
#    def __init__(self):
#        engine = db_connect()
#        create_dmoz_table(engine)
#        self.Session = sessionmaker(bind=engine)
#  
#    def process_item(self, item, spider):
#        session = self.Session()
#        dmoz = Dmoz(**item)
#        session.add(dmoz)
#        session.commit()
#        return item
#

#from scrapy import signals
#from twisted.enterprise import adbapi
#import MySQLdb
#import MySQLdb.cursors
#
#class MySQLStorePipeline(object):
#    def __init__(self):
#        self.dbpool = adbapi.ConnectionPool('MySQLdb',
#            db = 'security',
#            user = 'root',
#            passwd = 'lcy492',
#            cursorclass = MySQLdb.cursors.DictCursor,
#            charset = 'utf8',
#            use_unicode = False
#        )
    #def process_item(self, item, spider):
        #if 'time' in item: 
            #query = self.dbpool.runInteraction(self._conditional_insert, item)
        #elif '' in item:
            #query = self.dbpool.runInteraction(self._conditional_update, item)
        #else:
            #print "item has a error"
        #return item

#    def _conditional_insert(self, tx, item):
#        tx.execute('insert into share(title,link,time,content) values (%s, %s, %s, %s)',(item['title'], item['link'], item['time'], item['content']))
#
    #def _conditional_update(self, tx, item):
        #tx.execute('update user set mark=%s,count=%s where uid=%s',(item['mark'],item['count'],item['uid']))


