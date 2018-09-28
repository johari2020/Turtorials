#https://stackoverflow.com/questions/35166633/how-do-i-multiply-each-element-in-a-list-by-a-number/35166717

width = input("Width of multiplication table: ")
height = input ("Height of multiplication table: ")
w=(int(width)+1)
h=int(height)

t = "X"
b=list(range(0,w)) 

a=range(0,h)
meg = " "
for j in a:
    j+=1
    c=list(range(1,w)) 
    d = [i * (j) for i in c]
    print(str(list(d)), end = ' ' )
    print(" ")

