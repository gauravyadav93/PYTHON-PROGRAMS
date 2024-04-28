def square(n):
    ''' Takes in a number n, returns the square of n''' #here this line doesn't represent string 
    print(n**2)

square(5)
print(square.__doc__) #for access of docstring we use "doc" attribute.
#after changement in our docstrings our output,
#may be different but when we comment in a program or change it then there is no changement in our output.
#docstrings appears just after the definiton of a function.