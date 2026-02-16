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

# Phase 1
def save_user_data(name, **kwargs):
    # print("Name is ", name)
    # print("Kwargs are ", kwargs)
    # print things out as often as you can

    data = ""
    for key in kwargs: # looping technique
        # print("The key is ", key)
        value = kwargs[key]
        # print("The value is ", value)
        data = data + f"{key}:{value}\n"
        # print(data)
    
    with open(f'"{name}.txt", "w"') as file:
        file.write(data)

save_user_data("Ronnie")
# save_user_data("Samson", fav_color = "blue", fav_food = "beef")

def collect_user_data():
    name = input("Enter your name:")
    print("*******************")
    print(f"{name}, you can now fill your bio")
    print("Please enter categories and values")
    print("Done to exit")
    print("*******************")
    user_data = {}

    while True:
        category_name = input("Enter category name:")
        if category_name == "Done":
            break
        category_description = input("Enter your description:")
        user_data[category_name] = category_description
        #print(user_data)
    save_user_data(name, **user_data)

collect_user_data()