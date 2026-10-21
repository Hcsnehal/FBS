from abc  import ABC,abstractmethod
class employ(ABC):
    def __init__(self,id,name,sal):
        self.id=id 
        self.name=name 
        self.sal=sal 
    def display(self):
        print(f'id={self.id}  name={self.name}  sal={self.sal}')
    @abstractmethod    
    def calSal(self):
        pass
class Hr(employ):
    def __init__(self,id,name,sal,com):
        super().__init__(id,name,sal)
        self.com=com 
    def display(self):
        print(f'com={self.com}')  
        super().display()
    def calSal(self):
        return self.sal+self.com

class dev(employ):
    def __init__(self,id,name,sal,bonus):
        super().__init__(id,name,sal)
        self.bonus=bonus
    def display(self):
      
        super().display()
        print(f'bonus={self.bonus}')  
    def  calSal(self):
        return     

hr=Hr(2,'sham',899877,1000)
hr.display()

de=dev(3,'snehal',89009988,30000)
de.display()
print('salary of HR=',hr.calSal())
print('salary of developer =',de.calSal())
