from openpyxl import load_workbook
book = load_workbook("items.xlsx")
sheet = book.active


class Worker:
    def __init__(self, job, age, email, first_name, last_name, salary):
        self.job = job
        self.age = age
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

command = ""
while True:
    command = input("Enter the word worker to add new worker: ")
    if command == "worker":
        job = input("please enter job: ")
        age = input("please enter your age: ")
        email = input("please enter your email: ")
        first_name = input("please enter your first name: ")
        last_name = input("please enter your last name: ")
        salary = input("please enter your salary: ")

        user1=Worker(job, age, email, first_name, last_name, salary)
        print(user1.job)
        print(user1.age)
        print(user1.email)
        print(user1.first_name)
        print(user1.last_name)
        print(user1.salary)

    elif command == "exit":
        print("you have exited the worker program")
        break
    else:
        print("Please try again you have made a mistake")

#C:\Users\Alex\Documents