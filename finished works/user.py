class user:
    def __init__(self,firstname,lastname,middlename,gender,age):
        self.firstname=firstname
        self.lastname=lastname
        self.middlename=middlename
        self.gender=gender
        self.age=age
    def gendercheck(self):
        if str(self.gender).lower()=="male":
            return "Mr"
        elif str(self.gender).lower()=="female":
            return "Mrs"
        else:
            return "Not a valid gender"
    def initials_extract(self):
        initials=str(self.firstname[0]).upper() + "." + str(self.middlename[0]).upper() +" " +self.lastname
        return initials
    def Resolved(self):
        Prefix=self.gendercheck()
        return Prefix + " "+ self.initials_extract()
user1=user("Adelaja","Akimabogunje","Adeyinka","male",23)
ReturnedData=user1.Resolved()
print(ReturnedData) 