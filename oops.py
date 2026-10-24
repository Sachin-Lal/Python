class Student:
    name=""
    roll=""
    subjects=[]

    def study(self):
        print(self.name,"is studying.")

    def practical(self):
        print(self.name,"is doing practicals for",self.subjects[0])

ob1=Student()
ob1.name="Sachin"
ob1.roll="234"
ob1.subjects=["AI","Java","Python"]

ob2=Student()
ob2.name="Saptarshi"
ob2.roll="345"
ob2.subjects=["Automation","Maths","Backend Development"]

print("ob1")
ob1.study()
ob1.practical()
print("ob2")
ob2.study()
ob2.practical()