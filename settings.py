import os

service_name = "sms"
redis_queue = 'q:{}'.format(service_name)
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
