import random

#Add all elements in a list
def add_list(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + add_list(num_list[1:])

#Add elements in list using recursion
def add_nested_list(num_list):
    total = 0
    for element in num_list:
        if type(element) == type([]):
            total += add_nested_list(element)
        else:
            total += element
    return total

#Factorial of a number
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * (factorial(n-1))

ans1 = add_list([1,2,3,4,5,6])
ans2 = add_nested_list([1,2,3,[4,5],6])
ans3 = factorial(7)

print(ans1)
print(ans2)
print(ans3)

#List comprehension
list = [1,2,3]
new_list = [n+1 for n in list]
print(new_list)

name = "Angela"
name_list = [letter for letter in name]
print(name_list)

num_list = range(1,5)
doubled_list = [num*2 for num in range(1,5)] #or doubled_list = [num*2 for num in num_list]
print(doubled_list)

#names = ["Caroline", "Beth", "Alex", "Dave", "Eleanor", "Freddie", "Jonathan", "Emil", "Andrea"]
#new_names = [name.upper() for name in names if len(name) > 4]
#print(new_names)

names = ["Caroline", "Beth", "Alex", "Dave", "Eleanor", "Freddie", "Jonathan", "Emil", "Andrea"]

students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)

passed_students = {student:score for (student, score) in students_scores.items() if score >= 50}
print(passed_students)