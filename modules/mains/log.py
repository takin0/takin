#coding=utf-8 
import logging,os
import logging.config
path_base=os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
path_base=path_base.replace('\\', '/')
#print(path_base)
logging.config.fileConfig(path_base+'/conf/logging.conf')
#logger = logging.getLogger('admin')
logger = logging.getLogger('root')

if __name__=='__main__':    
    try:
        print(to445m)
    except:
        logger.exception('zz')
        logger0.exception('zz')
