# kwargs - key word arguments
# dicts -> js objects
# access values using bracket notation 

'''

def check_the_magic(**kwargs):
    print(f"The data type is: {type(kwargs)}")
    print(f"The content is: {kwargs}")
    print(f"Location is: ", {kwargs["location"]})

check_the_magic(name = "Joseph", age = 34, location = "Kenya")

By using ** (double asterick), you are telling Python: 
    "Take all these named arguments and pack them into a
    dictionary named kwargs." 
Now that you see the "dictionary" secret, here is how to build your
Universal Profile Builder project.

'''