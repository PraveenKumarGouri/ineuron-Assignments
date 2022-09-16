import logging
logging.basicConfig(filename='loginforlower.log',filemode="w",level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s  %(message)s')
class string_task:
    def string_lower(self, _Lstring):
        logging.info("WE are about to lower string")
        self._Lstring = _Lstring
        try:
            if len(_Lstring) == 0:
                raise ValueError("empty string")
                logging.error("empty string")
            else:
                str = _Lstring.lower()
                logging.info("lower string is %s: ", str)
                return str
        except Exception as e:
            logging.exception(e)
str_object = string_task()
b="WE are about to lower String"
a=str_object.string_lower(b)
print(b)




