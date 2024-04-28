n = int(input("enter the value of n:-"))
for i in range(1,n+1):
    for j in range(n,i,-1):
        print("",end="")
    for k in range(0,i):
        print("#",end="")
    print() 
    #OR

def staircase(n):
    for i in range(1,n+1):
        s = "#"*i
        print(s.rjust(n))
(staircase(4))