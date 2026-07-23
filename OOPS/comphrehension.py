# list comprehension is a concise way to create lists
#syntax : [expression for item in iterable if condition]

# using for loop only [not concise]

l = [] 
for i in range (1,51):
    if i % 2 == 0:
        l.append(i)
print(l)



# using list comprehension
# syntax : [expression for item in iterable if condition]

l1 = [i for i in range(1,51) if i%2 == 0]
print(l1)


# using dict comprehension
l2 = {i:i**2 for i in range(1,11) }
print(l2)

