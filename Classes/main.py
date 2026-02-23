# Classes
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

# Creating an instance
ronnie_nyakwama = Student("Ronnie Nyakwama", 26, "SE-FT16")
tracy_kwamboka = Student("Tracy Kwamboka", 21, "CS-PT14")

print(ronnie_nyakwama.name)
print(tracy_kwamboka.course)