class Jiujitsu:
    def __init__(self, first_name, last_name, age, belt, dojo, weight, height):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.belt = belt
        self.dojo = dojo
        self.weight = weight
        self.height = height

command = ""
while True:
    command = input("Enter the word jiujitsu to register to tournament: ")
    if command == "  ":
        first_name = input("please enter your name: ")
        last_name = input("please enter your last name: ")
        age = input("please enter your age: ")
        belt = input("please enter your belt color: ")
        dojo = input("please enter your Dojo: ")
        weight = input("please enter your weight: ")
        height = input("please enter your height: ")

        user1=Jiujitsu(first_name, last_name, age, belt, dojo, weight, height)
        print(user1.first_name)
        print(user1.last_name)
        print(user1.age)
        print(user1.belt)
        print(user1.dojo)
        print(user1.weight)
        print(user1.height)

    elif command == "exit":
        print("you have exited the tournament program")
        break
    else:
        print("Please try again you have made a mistake")



