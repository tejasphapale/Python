# Maximum in the array using user input...
n=int(input("Enter the numbers of element :"))
arr=[]
for i in range(n):
   element=int(input("ENter elements: "))
   arr.append(element)
max=arr[0]
for num in arr:
   if num>max:
      max=num
print("max element is:",max)
