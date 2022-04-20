import logging
import sys
from uvicorn import Config, Server
from loguru import logger
from server_config.config import Settings


class InterceptHandler(logging.Handler):
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger_text = record.getMessage().split(" - ")
        if len(logger_text) > 1:
            if logger_text[1] != '"GET /healthcheck HTTP/1.1" 200':
                logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())
        else:
            logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())



def setup_logging():
    logging.root.handlers = [InterceptHandler()]
    logging.root.setLevel(logging.getLevelName("INFO"))

    for name in logging.root.manager.loggerDict.keys():
        logging.getLogger(name).handlers = []
        logging.getLogger(name).propagate = True

    logger.configure(handlers=[{"sink": sys.stdout, "serialize": False}])


if __name__ == "__main__":
    try:
        server = Server(
            Config("init_application:application",
                   host=Settings.HTTP_SERVER_HOST,
                   port=Settings.HTTP_SERVER_PORT,
                   workers=Settings.COUNT_WORKERS_UVICORN,
                   debug=False)
        )
        setup_logging()
        server.run()
    except Exception as e:
        print(e, flush=True)
        exit(1)