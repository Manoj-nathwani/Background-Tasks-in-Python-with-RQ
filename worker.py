from handlers import *

print('Processing messages')
while True:
    message = service.get_next_message_to_process()
    print("Processing message '{}'".format(message))
    service.process_handler(**message)
