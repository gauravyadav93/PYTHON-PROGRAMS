import time
greet = time.strftime('%H:%M:%S')
greet = int(time.strftime('%H'))
# greet = int(input("enter hour: "))
print(greet)

if(4<=greet<12):
    print("good morning sir")
elif(12<=greet<17):
    print("good evening")
else:
    print("good night")
