from handlers import *

print('Processing messages')
while True:
    message = service.get_next_message_to_process()
    print('Started processing message {}'.format(message))
    service.process_handler(**message)
    print('Finished processing message {}'.format(message))
