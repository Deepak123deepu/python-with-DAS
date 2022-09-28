"""
- encapsulation
- adc - abstract base class (python module)
"""

# encapsulation 

"""
en capsul ation

we need to make our data as a capsul

- weather app (api -passcode)

1. public 
2. private
    1. private varb
    2. private methods 
conlu:

you can not use private varb, private methods outside class 
but you can use them inside class. 
"""

import sys


class system:

    def __init__(self, name, ram):
        self.name = name
        self.ram = ram
        self.ipadd = '0.0.0.0' # private varb

    def __getIp(self):
        print(self.ipadd)

    def getinfo(self):
        print(self.name)
        print(self.ram)
        self.__getIp()

   

    
s1 = system("dell", 8)
# s1.ram = 50
# s1.__ipadd = '192.123.45.6'
s1.getinfo()


print("------------------------------------------------")


"""
adc - abstract base class (python module)

- abstract class - if a class contain abstract methods then it is called abs class 
- abstract methods - if a methods has only def but not impementation

1. you can never create a obj for abstract class 
2. when you inhert a abc class you should impement abc method 
"""
print("----------- abstract class ouput -----------")

from abc import ABC, abstractmethod

class system(ABC):
    @abstractmethod
    def getCap(self):
        print("it will have ram and rom")
        print("it can run programs")
    
    @abstractmethod
    def emotionWithSys(self):
        pass

class phone(system):
    def getCap(self):
        return super().getCap()
    def emotionWithSys(self):
        print("i am happy with systhem cap's")
    def getCamInfo(self):
        print("this is will 30px cam")

pho1 = phone()
pho1.getCamInfo()
pho1.getCap()

