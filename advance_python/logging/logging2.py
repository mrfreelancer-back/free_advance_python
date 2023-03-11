import logging

logging.basicConfig(level=logging.DEBUG, filename='logging.log', filemode='w')

logging.debug('debug!')
logging.info('info...')
logging.warning('Warning!!!')
logging.error('An error!!!')
logging.critical('oooh! critical!!')
print('Go to logging.log!')