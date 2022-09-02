import logging

logging.basicConfig(filename="test5.log",level=logging.INFO,format='%(asctime)s %(name)s %(levelname)s %(message)s')

try:
    with open("sudh.txt", "r"):
        logging.info("successfully it has read the file")
except Exception as e:
    logging.error(e)
    logging.critical("This is situation for us")
    logging.error(e)
    logging.exception(e)
