# max element in the array...

arr = [12, 45, 23, 67, 89, 34]
max_element = arr[0]
for num in arr:
    if num > max_element:
        max_element = num
print("Largest element in the array is:", max_element)

