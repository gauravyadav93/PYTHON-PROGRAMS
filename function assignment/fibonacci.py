'''n = int(input("how many terms:-"))
n1, n2 = 0, 1
count = 0

if n<=0:
    print("enter a positive number:-")
elif n == 1:
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(n1)
        nth = n1 + n2
       # update values
        n1 = n2
        n2 = nth
        count += 1'''
def verify(num1,num2):
    if num1 > num2:
        return num1
    elif num1 == num2:
        return 1
    else:
        return num2

def display(arg1,arg2):
    if(verify(arg1,arg2)==arg1):
        print("A")
    elif(verify(arg1,arg2)==1):
        print("C")
    else:
        print("B")

display(1000,3500)



