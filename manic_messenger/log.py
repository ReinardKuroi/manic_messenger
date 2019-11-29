import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stdout = logging.StreamHandler()
stdout.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')
stdout.setFormatter(formatter)
logger.addHandler(stdout)
