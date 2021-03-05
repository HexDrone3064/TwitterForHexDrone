from logging import INFO, DEBUG, WARNING, ERROR
from logging import getLogger, StreamHandler, Formatter


formatter = Formatter('%(asctime)s [%(levelname)s] %(filename)s L%(lineno)d: %(message)s')


def get_logger(name: str, level: int = DEBUG):
    """
    StreamHandlerを適用したLoggerを取得する
    :param name: __name__
    :param level: INFO, DEBUG, WARNING, ERROR
    :return: Logger
    """
    logger = getLogger(name)
    logger.setLevel(level)
    handler = StreamHandler()
    handler.setLevel(level)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.propagate = False
    return logger
