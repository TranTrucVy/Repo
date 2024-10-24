import os
import logging

class Log_Maker:
    @staticmethod
    def log_gen(filename="C:/Users/trucv/PycharmProjects/nopEcomerce/logs/statuss.log", level=logging.INFO, 
                logformat='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
                datefmt='%H:%M:%S'):
        # Remove any previous logging handlers
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        
        logging.basicConfig(
            filename=filename,
            level=level,
            format=logformat,
            datefmt=datefmt,
        )
        logger = logging.getLogger()
        return logger
