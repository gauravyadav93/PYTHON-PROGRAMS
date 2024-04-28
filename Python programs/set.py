s ={2, 3, 4, 3}    #set avoid reptition of items.
print(s, type(s))

#for an empty set we can not use {}

h = set()
print(type(h))

# for accessing an item from set we use for loop

info = {'carla', 20, False, 5.9, 19}
for value in info:
    print(value)

#set methods in python. sets in python are same as in our mathematics
#we are using union() for joining two sets

s1 = {1, 2, 3, 4}
s2 = {1, 5, 3, 6, 7}
s3 = s1.union(s2)
print(s3) # or print(s1.union(s2))

# we are using intersection for common values b/w two sets.

print(s1.intersection(s2))

# for updating sets we use update() function 

s1.update(s2) # this will help in when some elements present in s2 but not in s1.
print(s1, s2)

# s1.intersection_update(s2) #first it will take common values b/w two sets then after add those elements which are not in s1 
# print(s1)

# symmetric difference is used for uncommon values b/w two sets.

print(s1.symmetric_difference(s2))

#using difference() and difference_update()    

cities = {'tokyo','madrid','berlin','delhi'}
cities2 = {'tokyo','seoul','kabul','delhi'}
cities3 = cities.difference(cities2)
# cities3 = cities.difference_update(cities2)
print(cities3)  # something like (a-b)

#similarly  isdisjoint() function is used when there is no common values b/w two sets, then it will return True else false.

# issuperset() function helps in when we have to check whether a set contained in another set or not.if contained then true.
