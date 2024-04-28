from functools import reduce

n1 = [1, 2, 3, 4, 5]
# def mysum(x, y):
#     return x + y
# sum = reduce(mysum, n1)
# print(sum)

# we can also use lambda function

sum1 = reduce(lambda x,y:x+y, n1)  # 1+2 = 3, 3+3=6, 6+4=10,10+5=15
print(sum1)