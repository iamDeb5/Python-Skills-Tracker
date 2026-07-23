# lambda function is a small anonymous function
# syntax : lambda arguments : expression

addition = lambda x,y : x+y

print(addition(10,20))

 
#if lambda function is used in if-else statement

check_even = lambda x : "Even" if x % 2 == 0 else "Odd"
print(check_even(10))
print(check_even(21))

