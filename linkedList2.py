
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

___data___|___nextadd__ -> ___data___|__nextadd___ -> ___data___|__nextadd____
                                          none                      None
        ^
        |


  70----->30----->20----->100----->   
                    ^ 
                    |  

0       1       2        3       4       5
90----->70----->120--->30----->20----->100----->
                ^
                |

         120 ---> 

"""


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
    def del_at_begining(self):
        self.head = self.head.nextadd
        return 
        
    # del at ending

    def getLengthOfLL(self):

        count = 0 
        tempIter = self.head 

        while tempIter:
            count = count + 1 # count += 1
            tempIter = tempIter.nextadd

        return count 

    def del_at_ending(self):

        tempIter = self.head
        count = 0 

        while tempIter:
            if count == (self.getLengthOfLL() - 1 ) -1 : #(self.getLengthOfLL() - 1 this is to get the last element) -1 -> to get the last secound element 
                tempIter.nextadd = tempIter.nextadd.nextadd 
                  # 20.(100 add)  = 20.(100 add)
                  #      none   <--    100.(none)  
                break
            tempIter = tempIter.nextadd
            count = count + 1



    # insert at any given index 
    def insertAtAnyGivenIndex(self, index, data): # -> O(n)
        
        if index <0 or index> self.getLengthOfLL():
            print("the size is out of index please check")
            return 
        
        count = 0 
        tempItrer = self.head

        while tempItrer:
            if count == index - 1:
                node = Node(data, tempItrer.nextadd)
                tempItrer.nextadd = node
                break

            tempItrer = tempItrer.nextadd
            count += 1


    # del at any given index 
    def delAtAnyGivenIndex(self, index):
        
        if index<0 or index>self.getLengthOfLL():
            print("the size is out of index please check")
            return

        count = 0
        tempIter = self.head 
        while tempIter:
            if count == index - 1:
                tempIter.nextadd = tempIter.nextadd.nextadd 
                break 
            tempIter = tempIter.nextadd
            count += 1 
    
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

# ll1.del_at_begining()
print(ll1.getLengthOfLL())

# ll1.del_at_ending()


ll1.insertAtAnyGivenIndex(2,120)
ll1.delAtAnyGivenIndex(2)

ll1.print()








    
    
        

