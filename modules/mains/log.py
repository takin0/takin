#coding=utf-8 
import os,logging
import logging.config
path_base=os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
path_base=path_base.replace('\\', '/')

logging.config.fileConfig(path_base+'/conf/logging.conf')
logger = logging.getLogger('file')
loggerp = logging.getLogger('conslo')


if __name__=='__main__':

    
    try:
        print(to445m)
    except:
        logger.exception('zz')
        loggerp.exception('xx')
