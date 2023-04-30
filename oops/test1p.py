class person :
    def __init__(self,name,surname,eamil_id,year_of_birth):
        self.name=name
        self.surname=surname
        self.email_id=eamil_id
        self.year_of_birth=year_of_birth

anuj_var=person("praveen","gouri","praveen39.39.39@gmail.com",1999)
praveen=person("kumar","gouri","praveen39.39.39@gmail.com",1999)
print(praveen.name)