#!/usr/bin/env python
# coding: utf-8

# In[1]:


from logging import handlers
import time
import logging
import sys 



# log檔的格式設定
class Logger(object):
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }

    def __init__(self,filename,level,when='D',fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)
        self.logger.setLevel(self.level_relations.get(level))
        
        if not self.logger.handlers:
            th = handlers.TimedRotatingFileHandler(filename=filename,when=when,encoding='utf-8')#往檔案裡寫入#指定間隔時間自動生成檔案的處理器
    
            th.setFormatter(format_str)
            self.logger.addHandler(th)

