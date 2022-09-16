import logging

logging.basicConfig(filename='loginfor.log',filemode="w",level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s  %(message)s')

class string_task:
    def string_split(self, _string):
        logging.info("WE are about to split string")
        self._string = _string
        try:
            if len(_string) == 0:
                raise ValueError("empty string")
                logging.error("empty string")
            else:
                str = _string.upper()
                str1 = str.split()
                logging.info("Split string is %s: ", str1)
                return str1
        except Exception as e:
            logging.exception(e)
str_object = string_task()
str_object.string_split("WE are about to split string")





