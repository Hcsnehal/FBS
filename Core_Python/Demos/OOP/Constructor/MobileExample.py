class mobile:
    def __init__(self,brand,model,price):
       self.brand=brand
       self.model=model 
       self.price=price 

    def getBrand(self):
        return self.brand   
    def setBrand(self,newbrand):
        self.brand=newbrand

    def getModel(self):
        return self.model 
    def setModel(self,newmodel):
        self.model=newmodel 

    def getPrice(self):
        return self.price 
    def setPrice(self,newprice):
        self.price=newprice 

    def display(self):
        print(f"Brand={self.brand}  model={self.model}  price={self.price}")    

m1=mobile('samgsung' ,'s25' , 900000) 
m1.setPrice(1000000)          
m1.display()        
       