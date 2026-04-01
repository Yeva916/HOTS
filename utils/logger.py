import logging
from constants import LOG_FORMAT

def get_logger(name):
    logging.basicConfig(format=LOG_FORMAT)
    return logging.getLogger(name)
print(0)
