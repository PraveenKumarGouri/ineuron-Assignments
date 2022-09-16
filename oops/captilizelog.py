import logging
logging.basicConfig(filename="loggcaptitalize",filemode="w",level=logging.DEBUG,format='%(asctime)s %(levelname)s %(name)s  %(message)s')
class string_task:
    def string_cap(self,Cstring):
        logging.info("This is a way to captalize")
        self.Cstring=Cstring
        try:
            if len(Cstring)==0:
                raise ValueError("Empty String")
                logging.error("This is error")
            else:
                str = Cstring.title()
                logging.info("this is a way to captilize")
        except Exception as e:
            logging.exception(e)
string_object=string_task()
a="This is a way of captilization"
k=string_object.string_cap(a)
print(k)
