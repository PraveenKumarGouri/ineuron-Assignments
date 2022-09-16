import logging

logging.basicConfig(filename='loginfo.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s  %(message)s')
class string_task:
    # Extract string
    def string_extract(self, ext_string):
        logging.info("WE are about to extract string from index one to index 300 with a jump of 3")
        self.ext_string = ext_string
        try:
            if len(ext_string) == 0:
                raise ValueError("empty string")
                logging.error("empty string")
            else:
                str = ext_string[::2]
                logging.info("Extracted string is %s: ", str)
                return str
        except Exception as e:
            logging.exception(e)
str_object = string_task()
str_object.string_extract("WE are about to extract string from index one to index 300 with a jump of 3")
print()

