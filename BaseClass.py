import logging


class  BaseClass:

   def getLogger(self):
       loggerName = inspect.stack()[1][2]
       logger = logging.getLogger(__name__)

       filerHandler = logging.FileHandler('logfile.log')
       formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
       filerHandler.setFormatter(formatter)
       logger.addHandler(filerHandler)

       logger.setLevel(logging.DEBUG)
       return  logger