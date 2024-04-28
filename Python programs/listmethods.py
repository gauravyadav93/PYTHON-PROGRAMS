#using .append() we can add a value at the end of our previous lists.
l = [1, 4, 2, 6, 10]
print(l)
l.append(7)  
print(l)


#using .sort()
l = [1, 4, 2, 6, 10]
print(l)
l.sort()  #it will return the value in ascending order.
l.sort(reverse = True)  #it will return the value in descending  order.
print(l)

#using .reverse() it will flip our lists elements.
l = [1, 4, 2, 6, 10]
l.reverse()
print(l)

#using .index() this method returns the index of the first occurence of the list item.
l = [1, 4, 2, 6, 10]
print(l.index(6))

#using .count() this returns the count of the number  of items with the given value.
l = [1, 4, 2, 1, 6, 10]
print(l.count(1))

#using .copy() this returns the copy of the list. this can be used to modify the operations on the list without modifying the original list.
l = [1, 4, 2, 1, 6, 10]
m = l.copy()
m[0] = 5
print(m)

#using .insert() this method insert an item at the given index. user has to specify the index and the item to be inserted without the insert() method.
l = [1, 4, 2, 1, 6, 10]
l.insert(1, 200)
print(l)

#using .extend() this method adds an entire list or  any other collection datatype(set, tuples, dictionary) to the existing lists.
l = [1, 4, 2, 1, 6, 10]
m = [900, 800, 600]
l.extend(m)
print(l)

#concatenating two lists 
l = [1, 4, 2, 1, 6, 10]
m = [900, 800, 600]
k = l + m
print(k)