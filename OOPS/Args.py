def addition (*args):                        # *args is used to pass any number of arguments to the function
    sum = 0                                 # sum is initialized to 0
    for i in args:                          # for loop is used to iterate over the arguments
        sum = sum + i                       # sum is updated with the current argument

    print(sum)                              # sum is printed after the loop

print(addition(10,20))
print(addition(10,20,30,40,50))
print(addition(10,20,30,40,50,60,70,80,90,100))