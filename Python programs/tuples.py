#manipulating tuples
countries = ("spain", "Italy", "India", "England", "Germany")
print(type(countries), countries)  #we can change a tuple by changing it into a lists after changement we have to again convert into tuple.
temp = list(countries)
temp.append( "Russia" ) #adding item
temp.pop(3) #removing item
temp[2] = "Finland" #change item
countries = tuple(temp)
print(countries, type(countries))

