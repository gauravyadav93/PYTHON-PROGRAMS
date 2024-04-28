# def cube(x):
#     return x*x*x
# l =[1, 2, 3, 4]
# newl = [ ]
# for i in l:
#     newl.append(cube(i))
# print(newl)

#instead of writing above code we can use map function
# newl = list(map(cube, l))
# print(newl)

#instead of defining a cube function we can directly use lambda function

l = [1, 2, 3, 4, 5, 6]
newl1 = list(map(lambda x:x*x*x, l))
print(newl1) 