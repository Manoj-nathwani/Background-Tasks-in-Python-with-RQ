import settings, logging, json, redis

class Microservice(object):

    def __init__(self):
        self.handlers = {}
        self.r = redis.from_url(settings.redis_url)

    def register_handler(self, handler_name):
        def decorator(func):
            self.handlers[handler_name] = func
            return func
        return decorator

    def process_handler(self, handler_name, data):
        self.handlers[handler_name](**data)

    def announce(queue, message):
        logging.info("Announcing message '{}' to queue '{}'".format(
            queue, message
        ))
        self.r.rpush(settings.redis_queue, 'bar')

    def get_next_message_to_process(self):
        message = self.r.blpop(settings.redis_queue)[1]
        logging.info("Processing message '{}'".format(message))
        message = json.loads(message)
        return message