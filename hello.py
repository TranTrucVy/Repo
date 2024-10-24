import os
import logging
def log_gen(filename ="statuss.log",level=logging.INFO, 
            logformat='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
            datefmt='%H:%M:%S' ):
    
    logging.basicConfig(
        filename= filename,
        level=level,
        format= logformat,
        datefmt=datefmt,
    )
    
    logger = logging.getLogger()
    return logger

logger = log_gen(filename="C:/Users/trucv/PycharmProjects/nopEcomerce/logs/statuss.log")

logger.debug("Thiss iss debug mess")
logger.info("Thiss iss info mess")
logger.warning("Thiss iss warning mess")
logger.error("Thiss iss error mess")
logger.critical("Thiss iss critical mess")
