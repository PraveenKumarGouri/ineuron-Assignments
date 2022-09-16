class Person :

    def __init__(self,name,surname,emailID,year_of_birth):
        self.name= name
        self.surname= surname
        self.emailID = emailID
        self.year_of_birth=year_of_birth
anuj_var = Person("anuj","bandari","anuj@gmail.com",1994)
sudh = Person("sudhanshu","kumar","sudhanshu@gmail.com",23424)
gargi = Person("gargi","xyz","gargi@gmail.com",234224)
print(anuj_var.name)
print(sudh.surname)
print(gargi.emailID)
print(anuj_var.year_of_birth)
print(type(sudh))