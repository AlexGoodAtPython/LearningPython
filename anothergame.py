command = ""
while True:
    command = input("-")
    if command.lower() == "turn on":
        print("Magical phone has turned on.")
    elif command.lower() == "turn off":
        print("Magical phone has turned off.")
    elif command.lower() == "float":
        print("The magical phone is making everything float")
    elif command.lower() == "explode":
        print("Magical phone will make anything you point it at to explode")
    elif command.lower() == "fly":
        print("Magical phone is making you fly")
    elif command == "help":
        print("""
        turn on - to turn on the phon
        turn off - to turn off the phone
        float - makes stuff float
        fly - to make you fly
        explode - to explode the phone
        exit - you exit the phone program and once you do that it will not work anymore
        """)
    elif command == "explode":
        print("phone has exploded so it doesnt work anymore")
        break
    elif command == "exit":
        print("you have exited the phone program so phone doesnt work anymore")
        break
    else:
        print("Sorry i dont know what you mean")