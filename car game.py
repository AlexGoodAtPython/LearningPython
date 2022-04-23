command = ""
while True:
    command = input("-")
    if command.lower() == "start":
        print("Car started.")
    elif command.lower() == "stop":
        print("Car stopped.")
    elif command.lower() == "float":
        print("car is floating")
    elif command.lower() == "enter":
        print("you have entered the car")
    elif command.lower() == "explode":
        print("car has exploded!")
        break
    elif command == "help":
        print("""
        enter - to enter the car
        start - to start thew car
        stop - to stop the car
        explode - to explode the car
        float - to float the car
        exit - to exit the car
        """)
    elif command == "exit":
        print("you have exited the car")
        break
    else:
        print("Sorry i dont know what you mean")

