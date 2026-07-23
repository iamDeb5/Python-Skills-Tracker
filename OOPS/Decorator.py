# Decorator:- it is used to add extra features to an existing function without modifying the existing function

def decorate (func):            # func is an argument which can be any function
    def wrapper():              # wrapper is a function which is nested inside the decorate function and it is also called as inner function
        print("Something is before function")
        func()                  # func() is calling the function which is passed as an argument to the decorate function
        print("Something is after function")
    return wrapper              # wrapper is returned by the decorate function

@decorate           # means @decorate(hello) this is the syntactical sugar for it
def hello ():       # hello is a function which is passed as an argument to the decorate function
    print("Hello I am Debojyoti")

hello()


def sum(func):                                  # func is an argument which can be any function
    def wrapper(a,b):                         # wrapper is a function which is nested inside the sum function and it is also called as inner function
        print("The sum of two numbers is")
        func(a,b)                             # func(a,b) is calling the function which is passed as an argument to the sum function
        print("I am done with the addition")
    return wrapper                            # wrapper is returned by the sum function

@sum                                          # means @sum(addition) this is the syntactical sugar for it
def addition(a,b):                          # addition is a function which is passed as an argument to the sum function and it is also called as inner function
    print("The addition of two numbers is",a+b)

addition(10,20)


