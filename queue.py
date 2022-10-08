

# queue = []

# queue.insert(0,"new1")
# queue.insert(0,"new2")
# queue.insert(0,"new3")
# queue.insert(0,"new4")

# print(queue)

# print(queue.pop())
# print(queue.pop())
# print(queue.pop())


from collections import deque


mynewapp = deque()

mynewapp.appendleft("n1")
mynewapp.appendleft("n2")
mynewapp.appendleft("n3")






class queue:
    def __init__(self):
        self.myqueue = deque()

    def Enqueue(self, valu):
        return self.myqueue.appendleft(valu)

    def Dequeue(self):
        return self.myqueue.pop()

    def size(self):
        return len(self.myqueue)



app1 = queue()
app1.Enqueue([
    "http:/n1",
    "ipl update"
])
app1.Enqueue([
    "http:/n2",
    "odi update"
])
app1.Enqueue([
    "http:/n3",
    "cms update"
])

print(app1.size())

print(app1.Dequeue())
print(app1.Dequeue())








