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
        return current_year
anuj_var = Person("anuj","bandari")
sudh = Person("sudhanshu ","kumar")
gargi = Person("gargi","xyz")
print(anuj_var.age(2022))
s = "sudh"
s.upper()
