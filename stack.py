
"""

- stack 
- ques 
- ll (4 types)
- trees (2 types) (binary)
- graphs


python stack imp 

- list (not good)


1 -> 1*2 -> 2 -> 2*2 -> 4

6 time replace - O(n)

- collections 

to push(), pop() 
time comp -> O(1)(constan time comp)
travel -> O(n)




"""

MyWedapplication = []

MyWedapplication.append("main/") 
MyWedapplication.append("main/c++")
MyWedapplication.append("main/java")
MyWedapplication.append("main/python")

MyWedapplication.pop()
MyWedapplication.pop()
MyWedapplication.pop()

print(MyWedapplication)




from collections import deque

# stackContainer = deque()


# stackContainer.append("main/")
# stackContainer.append("main/c++")
# stackContainer.append("main/java")
# stackContainer.append("main/python")

# print(stackContainer)

# stackContainer.pop()

# print(stackContainer)




class Stack:

    def __init__(self):
        self.container = deque()

    def push(self,element):
        return self.container.append(element)   

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]    
    
    def getSizeOfStack(self):
        return len(self.container)


myStack = Stack()
myStack.push("main/")
myStack.push("main/c++")
myStack.push("main/java")
myStack.push("main/python")


print(myStack.pop())
print(myStack.pop())

print(myStack.getSizeOfStack())


"""
finding pivot index question example for time and spcae comp
and optimization 


time  comp  = 7720 ms

space comp = 14.4 mb

-> O(n^2)

for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
                break
            else:
                continue
 else:
       return -1

optmize 
time  comp  = 302 ms

space comp = 14.6 mb
-> O(n)

leftSUM = 0 
rightSUM = sum(lis) 

for i in range(len(lis)):
    rightSUM = rightSUM - lis[i]
    
    if leftSUM == rightSUM:
        print(i)
    
    leftSUM = leftSUM + lis[i]

print(-1)

"""

