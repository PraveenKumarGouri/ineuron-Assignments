import logging

logging.basicConfig(filename='loginfor.log',filemode="w",level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s  %(message)s')

class string_task:

    # Extract string
    def string_Reverse(self, Rev_String):
        logging.info("WE are about to extract string from index one to index 300 with a jump of 3")
        self.Rev_String = Rev_String
        try:
            if len(Rev_String) == 0:
                raise ValueError("empty string")
                logging.error("empty string")
            else:
                str = Rev_String[::-1]
                logging.info("Extracted string is : %s: ", str)
                return str
        except Exception as e:
            logging.exception(e)
str_object = string_task()
a="WE are about to extract string from index one to index 300 with a jump of 3"
b=str_object.string_Reverse(a)
print(b)