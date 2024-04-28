n = int(input())
res = []
grade = []
for i in range(n):
    name = input()
    mark = float(input()) #for storing [name, mark] in our res we use .append() 
    res.append([name, mark])
    grade.append(mark)
print(res)  # for finding the second lowest grade. for that we make a seperate grade list for storing grades only 
print(grade)  # for finding the second lowest grade. for that we make a seperate grade list for storing grades only 
# or we can initially add a grade list right after the res = [].     
grade = sorted(set(grade))  #sorted unique elements
print(grade)
m = grade[1] # here 1 is the second lowest grade in grade list.
print(m)
name = []
for val in res:
    if m==val[1]:
        name.append(val[0])
print(name)  #unsorted name       
name.sort()
print(name) # sorted 
for nm  in name:
    print(nm)        

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
