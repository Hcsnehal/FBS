class Emp:
    def __init__(self,id,name,sal):
        self.eid=id 
        self._name=name 
        self.__sal=sal
e1=Emp(101,'snehal',1000000)

# print(e1.eid)    #public everywhere in code
# print(e1._name)#protected available in class and subclass
# print(e1._name)  #not worked in python
# print(e1.__sal)        #only inside the class
print(e1._Emp__sal)