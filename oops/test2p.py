class person:

    def __init__(self,name,last,email,yob):
        self.name=name
        self.last=last
        self.email=email
        self.yob=yob
    def age(self,current_year):
        return current_year-self.yob
praveen=person("kumar", "gouri", "praveen39@gmail.com", 1999)
print(praveen.age(2023))
