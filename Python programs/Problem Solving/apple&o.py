lsta = []
lsto = []
counte = 0
counto = 0
a = 4
b =12
apple = [2,3,-4]
oranges = [3,-2,-4]
for i in apple:
    app = i+4
    lsta.append(app)
print(lsta)
for j in oranges:
    ora = j+12
    lsto.append(ora)
print(lsto)
for k in range(7, 11):
    for a in lsta:
        if (k == a):
            counte+=1
print(counte)
for k in range(7, 11):
    for n in lsto:
        if (k == n):
            counto+=1
print(counto)

