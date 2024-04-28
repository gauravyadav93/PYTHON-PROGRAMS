data = [1, 2, 45, "GAurav"]
data[2] = "counting"
print(data, type(data))
print(data[-3]) #negative indexing
print(data[len(data) - 3]) #converting into positive indexing
print(data[4-3]) #positive index
print(data[1]) #positive index

if 2 in data:      # by this we can find any value from our list
    print("yes")
else:                                #same thing can also be used for string
    print("no")

if "Aurav" in "GAurav":
    print("yes")   

#if we have to print all the values of a list.
print(data)
print(data[:])

#list comprehension
list = [i for i in range(4)]
print(list)
list = [i*i for i in range(10) if i%2==0]
print(list)

# python expression printing each element of a list.
for  x in [1, 2, 3]:
    print(x, end = " ")
    