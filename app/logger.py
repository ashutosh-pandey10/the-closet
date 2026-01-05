import logging

def get_logger(name="the_closet", logfile="execution_log.log"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        # Console output
        stream_handler = logging.StreamHandler()
        stream_format = logging.Formatter('[%(asctime)s %(levelname)s]: %(name)s, - %(message)s')
        stream_handler.setFormatter(stream_format)
        logger.addHandler(stream_handler)

        # File output
        file_handler = logging.FileHandler(logfile)
        file_format = logging.Formatter('[%(asctime)s %(levelname)s]: %(name)s - %(message)s')
        file_handler.setFormatter(file_format)
        logger.addHandler(file_handler)
    return logger

logger = get_logger()
