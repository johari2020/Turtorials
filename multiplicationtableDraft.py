width = input("Width of multiplication table: ")
height = input ("Height of multiplication table: ")
h = int(height)
w = int(width) 
i=0
a = range(i,w)
b = range(i,h)

l = list(range(1,w))
m = list(range(1,h))

i=0
t = "X"
    
    
for i in b:
    i+=i-1
    print(t)