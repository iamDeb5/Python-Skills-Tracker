# Find the greatest element and print its index too

list_of_numbers = [45, 23, 56, 89, 12, 78, 34, 67, 90, 55]

largest = list_of_numbers[0]
index = 0

for i in range(len(list_of_numbers)):
    if list_of_numbers[i] > largest:
        largest = list_of_numbers[i]
        index = i

print(f"The largest element is {largest} and its index is {index}")



