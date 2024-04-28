for i in range(12):            #using continue statement
   if(i == 10):
        print("skip the iteration")
        continue
   print("5 *", i, "=", 5 * i)

print()
    


for i in range(12):             #using break statement
   if(i == 11):
        break
   print("5 *", i, "=", 5 * i)
print(" Leave the loop")    

print()


while True:                    #emulating do-while loop in python
    number = int(input("enter a positive number:"))
    print(number)
    if not number>0:
        break