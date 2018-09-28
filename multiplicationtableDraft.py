#https://stackoverflow.com/questions/35166633/how-do-i-multiply-each-element-in-a-list-by-a-number/35166717

width = input("Width of multiplication table: ")
height = input ("Height of multiplication table: ")
w=(int(width)+1)
h=int(height)

t = "X"
b=list(range(0,w)) 

a=range(0,h)
for j in a:
    meg=""
    j+=1
    c=list(range(1,w)) 
    d = [i * (j) for i in c]
    for k in d:
        meg = meg + str(k) + " "
    print(meg)
    #print((d), end = ' ' )
    
    #print(" ")

