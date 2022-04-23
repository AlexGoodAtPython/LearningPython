class Person:
    def __init__(self, age, weight, height, first_name, last_name, catch_phrase):
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name
        self.catch_phrase = catch_phrase

user=Person(25,70,177,"alex","Guncet","you either die a hero or live long enough to become the villain")
print(user.age)
print(user.weight)
print(user.height)
print(user.first_name)
print(user.last_name)
print(user.catch_phrase)



