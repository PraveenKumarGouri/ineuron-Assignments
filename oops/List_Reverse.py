import logging
logging.basicConfig(filename="ListRev.log",filemode="w",level=logging.DEBUG,format='%(asctime)s %(levelname)s %(name)s  %(message)s')
class List_task:
    def Listrev(self,listreverse):
        logging.info("this is for demo")
        self.listreverse=listreverse
        try:
            if len(listreverse) == 0:
                raise ValueError("list is empty")
                logging.info ("this is for information")
            else:
                listreverse = list(listreverse)
                listreverse.reverse()
                #listreverse = ''.join(listreverse)
                logging.info("this is for visual")
            return listreverse
        except Exception as e:
            logging.exception(e)
string_object=List_task()
a = ["ram","shaym", "sita"]
k=string_object.Listrev(a)
print(k)

