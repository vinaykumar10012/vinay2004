class stack:
    def __init__(self):
        self.items=[]

    def isempty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return(len(self.items))
s=stack()

print('stack operation example')
print(s.isempty())
s.push(40)
print(s.peek())
s.push(30)
print(s.peek())
s.push(10)
print(s.peek())
print(s.size())
s.push('pyton')
print(s.peek())
s.push(True)
print(s.size())
print(s.isempty())
s.push(11.5)
#print(s.())
print(s.size())
