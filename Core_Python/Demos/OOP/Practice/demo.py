class Employee:
     company_name='fbs' #static variable  
     @staticmethod
     def St_method():   
         print('im from satic method')               

     def __init__(self,id,name,sal):
            self.id=id
            self.name=name
            self.sal=sal
    # def initioliseStae(self,id,name,sal):
    #     self.id=id
    #     self.name=name
    #     self.sal=sal
     def getId(self):
        return self.Id
     def setName(self,newId):
        self.Id=newId

     def getName(self):
         return self.name 
     def setName(self,newName):
         self.name=newName 

     def getSal(self):
         return self.sal 
     def setSal(self,newSal):
         self.sal=newSal   
       
     def display(self):
        print(f'Eid= {self.id}\t name={self.name} \t Sal={self.sal}')
e1=Employee(12,"Sinu",123456)
e2=Employee(1,"Pravin",123456)
e1.St_method()