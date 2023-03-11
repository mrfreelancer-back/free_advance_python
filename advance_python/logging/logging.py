import logging

logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')

logging.debug('A debug message...')
logging.info('An info message...')
logging.error('An error message...')
logging.warning('A warning message...')
logging.critical('A critical message...')
