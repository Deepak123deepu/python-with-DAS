
# from collections import deque

# class Stack:

#     def __init__(self):
#         self.container = deque()

#     def push(self,element):
#         return self.container.append(element)   

#     def pop(self):
#         return self.container.pop()

#     def peek(self):
#         return self.container[-1]    
    
#     def getSizeOfStack(self):
#         return len(self.container)

    


# """
# "we are making it"
# -> 
# "ti gnikam era ew"
# ti gnikam era ew
# """

# givenString = "we are making it"

# stack = Stack()

# for i in givenString:
#     stack.push(i)
    
# res = ''
# while stack.getSizeOfStack() != 0:
#     res = res + stack.pop()

# print(res)


"""
LL imp

___data___|___nextadd__ -> __data___|__nextadd___ -> __data___|__nextadd____
                                                                None
        ^
        |
"""

from os import link
from tempfile import tempdir


class Node:
    def __init__(self, data = None , nextadd= None):
        self.data = data
        self.nextadd = nextadd

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head == None:
            print("linkedlist is empty")

        tempIterator = self.head
        linkledlist = ''
        while tempIterator:
            linkledlist = linkledlist + str(tempIterator.data) + "----->"
            tempIterator = tempIterator.nextadd

        print(linkledlist)

    # insert at begining
    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node 

    # insrt at ending 
    def insert_at_ending(self, data):
        # this is when your linkedlist is empty 
        if self.head == None:
            self.head = Node(data, None)
            return

        tempIter = self.head 

        while tempIter.nextadd:
            tempIter = tempIter.nextadd 

        tempIter.nextadd = Node(data,None)
    

    # del at begining 
    # del at ending
    
"""
task
list = [1,2,3,4,5]
convert to inkedllist 
"""

ll1 = LinkedList()
ll1.insert_at_begining(20)
ll1.insert_at_begining(30)
ll1.insert_at_begining(70)
ll1.insert_at_begining(90)

ll1.insert_at_ending(100)


ll1.print()








    
    
        

