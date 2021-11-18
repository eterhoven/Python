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