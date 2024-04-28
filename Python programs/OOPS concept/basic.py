class Person:
    name = "Gaurav"
    occupation = "Software engineer "
    networth = 10
    age = 23
    def info(self):  # here the meaning of self is that the object on which this method is called by.
        print(f"{self.name} is a {self.occupation}")  # here we are using f string
a = Person()
a.name = "shubham"  # we are using a.name for changing the name of an object of a class 
a.occupation = "Data Scientist"
a.info()
#print(Person.name,Person.occupation)

# we can simply create a new person with his identities no need  to create new class again and again 

b = Person()
b.name = "Golu"
b.occupation = "Data scientist"
b.info()

# if we do not assign an individual identity to third person or any then it takes default value

c = Person()
c.info()