import logging

def setup_logger(name: str):
    logger = logging.getLogger(name)
    if not logger.handlers:
        # File handler
        file_handler = logging.FileHandler(f'{name}.log')
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        logger.setLevel(logging.INFO)
    return logger
