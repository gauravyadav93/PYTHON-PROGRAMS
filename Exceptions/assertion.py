def ValidAge(age):
    assert age>0,"Please enter valid age"
    assert age<100,"Please enter valid age"
    print("you have entered valid age")
    print("rest of codee")
age = int(input("enter age"))
ValidAge(age)
