import  logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)

    filerHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    filerHandler.setFormatter(formatter)
    logger.addHandler(filerHandler)

    logger.setLevel(logging.DEBUG)
    logger.debug("A debug statement is executed")
    logger.info("information statement")
    logger.warning("something is in warning made")
    logger.error("A major error has happend")
    logger.critical("critical issue")
