import logging
import warnings
import inspect


class Log_generator:
    @staticmethod
    def log_gen():
        lon_name = inspect.stack()[1][3]
        logfile = logging.FileHandler("D:\\ct_17_batch_revision\\Pytest_Framework_By_Tushar_Sir\\Pytest_nopcommerce"
                                      "\\Logs\\nop_commerce.logs")
        format_ = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
        logfile.setFormatter(format_)
        logger = logging.getLogger(lon_name)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger


warnings.filterwarnings("ignore")
logging.getLogger("urllib3").setLevel(logging.ERROR)
