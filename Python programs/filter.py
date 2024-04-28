# WAP for using a filter function 

l = [1, 2, 3, 4, 5, 6]
# def filter_function(a):
#     return a>4
# newl = list(filter(filter_function, l))
# print(newl)

# we can use also lambda function

newl1 = list(filter(lambda a:a>4, l))
print(newl1)