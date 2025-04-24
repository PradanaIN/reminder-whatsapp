import logging

def setup_logger(name: str):
    logger = logging.getLogger(name)
    if not logger.handlers:  # Hindari duplikasi handler
        handler = logging.FileHandler(f'{name}.log')
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
    return logger
