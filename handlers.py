import settings
from utils.microservice import Microservice

service = Microservice()

@service.register_handler('send_sms_message')
def send_sms_message(potato, **kwargs):
    print('1'*10)

@service.register_handler('send_sms_message2')
def send_sms_message2(**kwargs):
    print('2'*10)

@service.register_handler('send_sms_message3')
def send_sms_message3(**kwargs):
    print('3'*10)
