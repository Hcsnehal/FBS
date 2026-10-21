#abstract method 
#1.need to implement compulsory in subclasses 
#2.no body only defination 

from abc import ABC, abstractmethod 
class Vehical(ABC):
    @abstractmethod 
    def stop():
        pass 
# v=Vehical()    #cant instantiate
class Bike(Vehical):
    def start(self):
        print('start method...')
    def stop(self):
        print('stop method')
b1=Bike()            
b1.start()
b1.stop()