

# 1. List (Ordered, Mutable, Allows Duplicates)
# use square [] brackets to define list 

fruits = ["apple", "guava", "orange"]

fruits.append("mango")

print(fruits)
print(fruits[2])
print(fruits[-2]) #it started bidirection also with negative index
print(fruits[-3])

my_list1 = [1, "a", True, 3.14]
print(type(my_list1))

my_list2 = [1, [4,5], True]
print(type(my_list2))

#slicing
print(my_list1[:2])
print(my_list1[:])

#creating list of squre..
squares = [x**2 for x in range(1, 6)]
print("Square lis is = ", squares)

# iteration

for fruite in fruits:
    print(fruite)

# using while

index = 0
while index < len(fruits):
    print(fruits[index])
    index+=1

# 2. Tuple (Ordered, Immutable, Allows Duplicates)
# use round () brackets to define Tuples

colors = ('red', 'green' , 'yellow')
print(colors)
print(colors[1])

# 3. Set (Unordered, Mutable, No Duplicates)
# use curly {} brackets to define the Set

unique_nums = {1,2,3,3,4,5}
unique_nums.add(6)

print(unique_nums)

# 4. Dictionary (Key-Value Pairs, Unordered in <3.7, Ordered in ≥3.7)

person = {'name' : 'Sach' , 'age' : 28}
print(person['name'])
person['age'] = 25