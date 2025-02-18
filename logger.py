import logging

def setup_logger(name: str):
    # Membuat handler untuk menulis log ke file
    handler = logging.FileHandler(f'{name}.log')
    handler.setLevel(logging.INFO)  # Set level log ke INFO (bisa ganti ke DEBUG, WARNING, dll)

    # Membuat formatter untuk format log
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Membuat logger dan menambahkan handler
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    
    return logger
