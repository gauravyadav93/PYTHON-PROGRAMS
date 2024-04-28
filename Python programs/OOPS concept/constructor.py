def div(a,b):
    div = a/b
    print(div)

def new_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner
div1 = new_div(div)
div1(1000,2000)
