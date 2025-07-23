# accept array from the user and display it...

n = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(n):
    element = int(input("Enter element {i+1}: "))
    arr.append(element)
total = 0
for num in arr:
    total += num
print("Sum of the array is:", total)

