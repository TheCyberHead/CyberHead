import logging, os

class Logger:
    def __init__(self, module):
        self.module = module

    def log(self, message):
        handlers = [logging.FileHandler("cyberhead.log"), logging.StreamHandler()]
        formater = f'[%(asctime)s] [{self.module}] [%(filename)s] [%(levelname)s] %(message)s'
        logging.basicConfig(level=logging.INFO, format=formater, handlers=handlers)

        logger = logging.getLogger(self.module)
        logger.info(message)
