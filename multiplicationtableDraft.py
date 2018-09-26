width = input("Width of multiplication table: ")
height = input ("Height of multiplication table: ")
w=int(width)
h=int(height)

t = "X"
    
b=range(0,w)
a=range(0,h)
for j in a:
    j+=j-1
    for i in b:
        i+=i-1
        print(t, end = ' ' )
    print(" ")