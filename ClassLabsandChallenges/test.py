user_input = input("Enter a string: ")
new_string = ""

for i in user_input:
    if i.lower() in "aeiou":
        new_string += "*"
    else:
        new_string += i

print(new_string)
        