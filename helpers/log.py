import logging
from helpers import config

def logger(module_name):
    log_file = config.get('default', 'LOG_FILE')
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
     # write log messages to console
    handler_console = logging.StreamHandler()
    handler_console.setLevel(logging.DEBUG)
    handler_console.setFormatter(formatter)
    logger.addHandler(handler_console)

    # write log messages to log file
    handler_file = logging.FileHandler(log_file)
    handler_file.setLevel(logging.DEBUG)
    handler_file.setFormatter(formatter)
    logger.addHandler(handler_file)

    
    return logger