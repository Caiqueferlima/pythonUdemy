list1 = [10, 50, 40, 80, 90]
list2 = [10, 50, 20, 70, 90]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) #Union
print(num1 - num2) #Difference
print(num1 ^ num2) #Symmetric Difference
print(num1 & num2) #And

# é possível criar um set assim como uma lista, usando {}
set1 = {1, 2, 3, 4, 5, 6}
set1.update([6, 7, 8, 9])
set1.discard(7)
set1.remove(1)
set1.add(3)

print()
print(set1)

