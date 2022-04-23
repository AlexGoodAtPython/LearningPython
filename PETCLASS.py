class Pet:
    def __init__(self, first_name, last_name, age, pet_breed, pet_name, pet_weight):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.pet_breed = pet_breed
        self.pet_name = pet_name
        self.pet_weight = pet_weight
        self.pet_age = pet_age

command = ""
while True:
    command = input("Enter the sentence i want to adopt a pet: ")
    if command == "i want to adopt a pet":
       first_name = input("please enter your name: ")
       last_name = input("please enter your last name: ")
       age = input("please enter your age: ")
       pet_breed = input("please enter your pet breed: ")
       pet_name = input("please enter your pet name: ")
       pet_weight = input("please enter your pets weight: ")
       pet_age = input("please enter your pets age")

       user1 = Pet(first_name, last_name, age, pet_breed, pet_name, pet_weight, pet_age)
       print(user1.first_name)
       print(user1.last_name)
       print(user1.age)
       print(user1.pet_breed)
       print(user1.pet_name)
       print(user1.pet_weight)
       print(user1.pet_age)



    elif command == "exit":
        print("you have exited the pet adoption program")
        break
    else:
        print("Please try again you have made a mistake")


