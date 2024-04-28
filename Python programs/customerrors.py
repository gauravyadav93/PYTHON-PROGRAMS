# a= int(input("enter the number: "))

# if(a<5 or a>9):
#     raise ValueError   # here we are raising custom valueerror.
# else:
#     print("matching with conditon")

b = input("enter the number: ")
if(b == "quit"):
    print("executed")
elif(int(b)<5 or int(b)>9):
    raise ValueError("number b/w 5 & 9")





