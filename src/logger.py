import logging

def init_logger():
    logger = logging.getLogger('py-injobs')
    logger.setLevel(logging.INFO)
    if not logger.handlers:
          formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
          console_handler = logging.StreamHandler()
          console_handler.setFormatter(formatter)
          logger.addHandler(console_handler)

    return logger
