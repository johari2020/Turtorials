height = input("Width of multiplication table: ")
width = input ("Height of multiplication table: ")
h = int(height)
w = int(width) 
i=0
a = range(i,h)
b = range(i,w)

l = list(range(1,w))
m = list(range(1,h))

i=0
t = "X"
    
    
for i in b:
    i+=i-1
    print(t*w)