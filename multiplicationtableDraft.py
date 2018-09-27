width = input("Width of multiplication table: ")
height = input ("Height of multiplication table: ")
w=int(width)
h=int(height)

t = "X"
b=list(range(0,w)) 

a=range(0,h)
for j in a:
    j+=j-1
    for i in b:
        i+=1
        c=list(range(1,i+1)) 
        print((c), end = ' ' )
    print(" ")
