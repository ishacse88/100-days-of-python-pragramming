list=[22,89,100,34]
print(max(list))
print(min(list))

list.reverse()
print("reversed list",list)

list.sort(reverse=True)
print("reversed list:", list)


a=sorted(list)
b=list.copy()
if sorted(list)==list.copy():
    print("list is sorted")
else:
    print("list is not sotred")

numbers = [22, 89, 100, 34]

# Remove duplicates (important in case of repeated numbers)
unique_numbers = list(set(numbers))

# Step 1: Find the largest and smallest
largest = max(unique_numbers)
smallest = min(unique_numbers)

# Step 2: Remove them from the list
unique_numbers.remove(largest)
unique_numbers.remove(smallest)

# Step 3: Find second largest and second smallest
second_largest = max(unique_numbers)
second_smallest = min(unique_numbers)

print("Second Largest:", second_largest)
print("Second Smallest:", second_smallest)






