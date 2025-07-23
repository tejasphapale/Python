# array of sum using split method...

user_input= input("enter numbers ")
numbers= list(map(int, user_input.split()))
array_sum= sum(numbers)
print("the sum of array:",array_sum)
