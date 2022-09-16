class Person :
    def __init__(praveen,name,surname,emailID,year_of_birth):
        praveen.name= name
        praveen.surname= surname
        praveen.emailID = emailID
        praveen.year_of_birth=year_of_birth

    def __init__(praveen,name,surname):
        praveen.name= name
        praveen.surname= surname

    def age(sudh,current_year):
        return current_year - sudh.year_of_birth
anuj_var = Person("anuj","bandari","anuj@gmail.com",1994)
sudh = Person("sudhanshu ","kumar","sudhanshu@gmail.com",23424)
gargi = Person("gargi","xyz","gargi@gmail.com",234224)
print(anuj_var.age(2022))
s = "sudh"
s.upper()
