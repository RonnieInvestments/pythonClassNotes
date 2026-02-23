'''
user_input = input("Enter a string: ")
new_string = ""

for i in user_input:
    if i.lower() in "aeiou":
        new_string += "*"
    else:
        new_string += i

print(new_string)
'''
# First five even numbers
my_list = []
for n in range(1,6):
    even_num = n * 2
    my_list.append(even_num)

'''
# print(my_list[2])
nums = [1, 2, 3, 4, 5]
nums.append(10)
print(nums)
'''

'''
Write a program that creates a list of named numbers containing the numbers from 1 to 10. 
Then use a loop to print all the elements in the list that are greater than 5.

numbers = list(range(1,11))
print(numbers)
numbers_greater_than_five = []
for number in numbers:
    if number > 5:
        numbers_greater_than_five.append(number)
print(numbers_greater_than_five)
'''

'''
# reverse method
numbers = list(range(1,6))
#print(numbers)
reversed_numbers = list(reversed(numbers))
print(reversed_numbers)
'''
'''
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(my_dict['age'])

person = {'name': 'Emma', 'age': 28}
person.update({'country': 'USA'})
print(person)


person = {'name': 'Alice', 'age': 25, 'city': 'London'}
person.pop('age')
print(person)
'''
# Creating the dictionary
my_dict = {
    'a': 1, 
    'b': 2, 
    'c': 3
}

# Looping through
for key, value in my_dict.items():
    print(f"{key}: {value}")