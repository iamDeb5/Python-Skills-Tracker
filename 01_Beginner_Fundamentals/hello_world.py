print("Hello World!") #This is the starting of learning language

# print("hello genz") Its a single line comment !!

"""Its a multi line comment"""

#Variable declaration

name = "Sher"
print(name)

FirstName = "Sheriyans" # Pascal Case Variable name declaration
print(FirstName)

lastName = "dotCom" #Camel Case Variable name declaration
print(lastName)

mobile_number = "91****4590" #Snake Case Variable name declaration
print(mobile_number)


#Data Types 

a = -34
print(type(a)) #Its a Integer type value

b = 55.9
print(type(b)) #Its a Float type value

c = 40/5
print(type(c)) #Its also a Float type value

d = 45j
print(type(d)) #Its a Complex type of value

#These 4 variable are example of Numbers Data Type

st = 'I am a String type of variable!'
print(type(st)) #Its a String type of value

bol = True
print(type(bol)) #Its a Boolean type value

"""String Indexing"""

index = "SHER CODER"

print(index[2])  #Positive indexing
print(index[-2]) #Negative indexing

"""String Slicing"""

print(index[0:4:1]) #slicing "sher" from index
print(index[5:10])  #slicing "coder" from index


"""Type Conversion"""

# a = -34
a = str(a)  #type will be convert to string
print(type(a)) 

z = "12"
z = int(z)  #type will be convert to integer

print(type(z))  


age = 21 

print("hello!! my name is",name,"and my age is",age)

print(f"Hello! My name is {name} and my age is {age}") # And formated string


"""INPUT FROM USER"""   # Default data type of input is string but we can covert the data types

# location = input("Where are you from?\n") # Taking input from user 
# print(f"This User is from {location}")    # Print the value

# age = int(input("What's your age....user ?"))   # Converting the string input to integer data type
# print(f"User's age is {age}")



"""There are 7 types of Arithmetic operators in pyton
    [ + , - , * , / , % , // , ** ]
"""

num1 = 15
num2 = 10

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2)
print(num1 // num2)
print(num1 ** num2)


"""Compund Assignment Operators"""

# num2 = num2 + 10 

num2 += 10  # num2 = num2(10) + 10 (20)
print(num2) 
num2 -= 10  # num2 = num2(20) - 10 (10)
print(num2) 
num2 *= 10  # num2 = num2(10) * 10 (100)
print(num2)
num2 /= 10  #num2 = num2(100) / 10 (10.0)
print(num2)

"""Comparison Operators""" #Always give a boolean value either "True" or "False"

x = 10
y = 10.2

print(x == y)   # False
print(x != y)   # True
print(x > y)    # False
print(x < y)    # True

print(x >= y)   # False
print(x <= y)   # True

"""Logical Operators""" 

#   And Operation

print(15 < 25 and 26 < 35 and 55 > 51)  # If all the operations are true then the final boolean value will be true in "And"

print(15 > 25 and 26 < 35 and 55 > 51)  # So its false 


#   OR Operation

print(15 != 15 or 21 == 24 or 15 > 10)  # If any one operation is true then the "OR" is true

#   Not operator

print(12 == 12) #this is obvious true

#but if i use not 

print(not 12 == 12)    # then it will be false. Not reverse the value from true to false and false to true
