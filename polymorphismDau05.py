"""

poly morph iasm
  |    |
 many forms   


- Duck typing -> python, js, php, prel
- op overloding 
- method overloading 
- method overriding 

"""

# x = 90 -> int 

# x = {"hey":"name plea"} -> dict 


"""
1. Duck typing

if there is a animal that looks like duck 
and swim like duck
and quacks like duck 
that it is a duck 

"""

# class firstBook():

#     def readContexts(self):
#         print("this is my first book")
#         print("title is 'no more love..!' ")

# class secoundBook():

#     def readContexts(self):
#         print("this is secoud book")
#         print("title is 'women are not good for health..!'")


# class reader:

#     def read(self, book):
#         book.readContexts()

# fb1 = firstBook()
# sb1 = secoundBook()

# reader1 = reader()
# reader1.read(sb1)


# class bike:
#     def onroad(self):
#         print("i can go on road")

# class car:
#     def onroad(self):
#         print("i can go on road")

# class bicycle:
#     def onroad(self):
#         print("i can go on road")

# class airways:
#     def onair(self):
#         print("i can go on air")

# for obj in bike(), car(), bicycle():
#     obj.onroad()


"""
2. oparate overloading
"""

# a = 2
# b = 3

# print(a)
# print(a - b)

# print(int.__str__(a))

from sys import flags


class emp:

    def __init__(self, sal, outSal):
        self.sal = sal
        self.outSal = outSal

    def __add__(self, empNext):
        normalSal = self.sal + empNext.sal
        outSal = self.outSal + empNext.outSal
        obj = emp(normalSal, outSal)
        return obj 

    def __str__(self):
        return f'emop normal sal is {self.sal} and outside sal is {self.outSal}'

    def __le__(self, obj):
        if self.sal <= obj.sal:
            return True 
        else:
            return False


emp1 = emp(20000, 30000)
emp2 = emp(50000, 60000)
emp3 = emp(60000, 90000)

boss = emp1 + emp2   # -> emp.__add__(emp1, emp2)

print(boss) # -> emp.__str__(boss) 
print(boss.outSal, boss.sal)


if emp2 <= emp3: # -> emp.__le__(emp1, emp2)
    print("emp3 is big")
else:
    print("emp2 is big")

    
    








