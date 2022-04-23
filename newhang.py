import random
import time

secret_word = ["ball", "doll", "golf", "secrets", "thief"]
word = random.choice(secret_word)
length = len(word)
name = input("What is your name: ")
print("Welcome "+name + " Best of luck!...")
time.sleep(2)
print("Test begins now...")
time.sleep(2)

count = 0
display = '*' * length


def hangman(count, display, word):
    limit = 3
    guess = input("This is Word: "+ display + " Enter your guess: ")
    if guess in word:
        index = word.find(guess)
        word = word[:index] + "*" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display)
    else:
        count+= 1
        if count == 1:
            print("Wrong input. " + str(limit - count) + "guess remaining")
            print(""
                  "    _______ \n"
                  "   |        \n" 
                  "   |        \n"
                  "   |        \n"
                  "   |        \n"
                  "   |        \n"
                  "   |        \n"
                  "___|___\n"


            )

        elif count == 2:
            print("Wrong input. " + str(limit - count) + "guess remaining")
            print(""
                  "    _______ \n"
                  "   |       |\n"
                  "   |       |\n"
                  "   |       |\n"
                  "   |        \n"
                  "   |        \n"
                  "   |        \n"
                  "___|___\n"


                  )

        elif count == 3:
            print("Wrong input. You are hanged")
            print(""
                  "    _______ \n"
                  "   |       |\n"
                  "   |       |\n"
                  "   |       |\n"
                  "   |       o\n"
                  "   |      /|\ \n"
                  "   |      / \ \n"
                  "___|___\n"


                  )

    if word == '*' * length:
        print("congrats! You have guessed the word!")
    elif count != limit:
        hangman(count, display, word)

hangman(count, display, word)