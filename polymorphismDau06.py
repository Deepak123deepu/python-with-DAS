"""

- method overloading 
- method overriding

"""



#    (---- method overloading ---- (not there in python, but we can make it happen))


class student(object):
    def __init__(self, rollno, name, fee):
        self.rollno = rollno
        self.name = name
        self.fee = fee
    

    def incre_marks(self, m1=12, m2=None, m3=None, m4 = None):
        # using none tech 
        totalMarks = 0 

        if m1!=None and m2!=None and m3!=None and m4!=None:
            totalMarks = m1 + m2 + m3 +m4
        elif m1!=None and m2!=None and m3!=None:
            totalMarks = m1+m2 +m3
        elif m1!=None and m2!=None:
            totalMarks = m1+m2
        else:
            totalMarks = m1 

        print(totalMarks)


s1 = student(121,'deep', 12000)
s1.incre_marks(12,)



#        (------- method overriding -------)

class car:

    def move(self):
        print("i am the car so i can move in rode")

class boat(car):

    def move(self):
        print("as i am boat i can move on water")

vech1 = boat()
vech1.move()



    


