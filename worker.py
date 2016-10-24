import logging

print('Processing messages')
logging.warn('Testing warning')
logging.error('Testing error')

from handlers import *

while True:
    print('processing message')
    logging.info('fwew')
    message = service.get_next_message_to_process()
    service.process_handler(**message)
