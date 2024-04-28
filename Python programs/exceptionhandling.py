# here we are printing multiplication table of  numbers.
a = input("enter the number: ")
print(f"multiplication table of {a} is: ")

for i in range(1, 11):
    print(f"{int(a)} X {i} = {int(a)*i}")


#use of try and except (if we do not want any hault in our program).

a = input("enter the number: ")   # here if we input a string in terminal, no error will be directly shown by terminal.
print(f"multiplication table of {a} is: ")

try:
  for i in range(1, 11):
    print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:  # here we can only use exception 
   print(e)   # here we can print "invalid input" means we can handle an specific type of error.

print("some imp lines of code")
print("end of program")    

#we can use this for multiple type of errors such as memory error, index error etc.

try:
    num = int(input("enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("number entered is not an integer.")
          
except IndexError:
 print("Index Error")