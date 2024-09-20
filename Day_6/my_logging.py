import logging

logging.basicConfig(filename='basicconfig.log',level= logging.DEBUG, format="%(asctime)s -%(levelname)s -%(message)s")

logging.debug('This is a debug message')
logging.info('This is a debug message')
logging.warning('This is a debug message')
logging.error('This is a debug message')
logging.critical('This is a debug message')

logger = logging.getLogger(('advancedconfig_logger'))
handler = logging.FileHandler