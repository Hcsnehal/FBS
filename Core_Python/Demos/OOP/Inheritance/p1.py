class emp:
    def calsal(salf):
        print('calculate emp sal')
class HR(emp):
    def calsal(self):
        print('calculate Hr sal')
class Admin(emp):
    def calsal(self):
        # print('cal admin salary ') 
              
h=HR()
a=Admin()
h.calsal()
a.calsal()

