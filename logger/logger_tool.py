import logging

log_file = "./logs/logfile.log"
log_level = logging.DEBUG
logging.basicConfig(
    level=log_level,
    filename=log_file,
    filemode="w",
    format="%(process)s | %(name)s | %(asctime)-15s | %(levelname)-8s | %(message)s",
)
logger = logging.getLogger(__name__)


class Logger:
    def wrap(self, pre, post):
        """ Wrapper """

        def decorate(func):
            """ Decorator """

            def call(*args, **kwargs):
                """ Actual wrapping """
                pre(func)
                result = func(*args, **kwargs)
                # logger.debug("Function result %s", result)
                post(func)
                return result

            return call

        # logger.debug("Function result %s", decorate)
        return decorate

    def entering(self, func):
        """ Pre function logging """
        logger.debug("Entered %s", func.__name__)

    def exiting(self, func):
        """ Post function logging """
        logger.debug("Exited  %s", func.__name__)
