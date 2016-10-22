import logging

print('processing message')
logging.info('fwew')

from handlers import *

while True:
    print('processing message')
    logging.info('fwew')
    message = service.get_next_message_to_process()
    service.process_handler(**message)
