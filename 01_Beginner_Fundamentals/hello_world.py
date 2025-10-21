print("Hello World!") #This is the starting of learning language

# print("hello genz") Its a single line comment !!

"""Its a multi line comment"""

#Variable declaration

name = "Sher"
print(name)

FirstName = "Sheriyans" #Pascal Case Variable name declaration
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
