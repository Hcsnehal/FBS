class Student:
    stu_count=0
    def __init__(self,name,rollno):
        self.name=name 
        self.rollno=rollno 
        Student.stu_count+=1
    def display(self):
        print(f'name={self.name}  rollno={self.rollno}')    

class placeStu(Student):
        def __init__(self, name, rollno,cname):
             super().__init__(name, rollno)
             self.cNaem=cname
        def display(self):
            print(f"CName={self.cNaem}",end=" ")
            super().display()     
                   

st=placeStu('rohot',5,'infosys')           
st.display()     

s=Student('snehal',101)
s1=Student('sinu',102)
s.display()
s1.display()

print(Student.stu_count)
