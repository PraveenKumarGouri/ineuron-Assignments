import logging
logging.basicConfig(filename="test4.log", level=logging.WARNING,format='%(asctime)s %(name)s %(levelname)s %(message)s' )
def divide(a,b):
    logging.info("The number entered by under is : %s and %s", a,b)
    try:
        logging.info("we are into function")
        div = a/b
        logging.info("we have compleated division")
        logging.info("result of code is %s",div)
        return div
    except Exception as e:
        logging.exception(e)
        print(e)


print(divide(3,0))
