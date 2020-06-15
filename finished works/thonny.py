class student:
    age=0
    matricno=''
    name=''
    gpa=0
    units=3
    cumpoint=0
    totalunits=0
    
    def __init__(self,studentname,matricno,age,gpa):
        self.name=studentname
        self.matricno=matricno
        self.age=age
        self.gpa=gpa
        self.totalunits=len(gpa)*self.units
    
    def studgpa(self):
        for x in self.gpa:
            if x>=70 and x<=100:
                point=5
                self.cumpoint+=(point*self.units)
            elif x>=60 and x<=69:
                point=4
                self.cumpoint+=(point*self.units)
            elif x>=50 and x<=59:
                point=3
                self.cumpoint+=(point*self.units)
            elif x>=40 and x<=49:
                point=2
                self.cumpoint+=(point*self.units)
            elif x>=30 and x<=39:
                point=1
                self.cumpoint+=(point*self.units)
            elif x>=0 and x<=29:
                point=0
        self.cumpoint+=(point*self.units)
        self.gpa=self.cumpoint/self.totalunits
        return self.gpa
    
    def forstudname(self):
        if self.name=="ADELAJA":
            return "Akinmabogunje Adelaja Adeyinka"
        else:
            return "He is not part of our class"
    
    def forstudname1(self):
        return self.name

student1=student("ADELAJA","cve090",25,[56,78,65,90,87,34,2,45,67])    
FirstGPA=student1.studgpa()
FirstStdName=student1.forstudname()
student2=student("olayiwola","cve345",45,[45,35,78,98,78,87,45,65,43,78,93])
SecondGPA=student2.studgpa()
SecondStdName=student2.forstudname1()

print("The GPA of {0} with matric number {1} who is {2} years old is  {3}".format(FirstStdName,student1.matricno,student1.age,student1.gpa))
print("The GPA of {0} with matric number {1} who is {2} years old is  {3}".format(SecondStdName,student2.matricno,student2.age,student2.gpa))