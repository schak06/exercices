
import random
#Task1
def f1():
        print("task1")
        dice_count = int(input("Enter how many dice to roll: "))
        total = 0
        for item in range(dice_count):
            roll = random.randint(1, 6)
            total += roll
        print(f"Sum of {dice_count} dice rolls: {total}")


#Task2
def f2() :
    print("Task2")
    numbers = []

    while True:
        question = input("Enter a number (empty string to quit): ")
        if question == "":
            break
        try:
            number:int = int(question)
            numbers.append(number)
        except ValueError:
            print("Invalid input, please enter an integer.")

    if numbers:
        numbers.sort(reverse=True)
        top_five = numbers[:5]
        print("Top five numbers in descending order:")
        for n in top_five:
            print(n)
    else:
        print("No numbers were entered.")

#Task 3
def f3() :
    print("Task3")
    number = int(input("Enter an integer: "))
    if number < 2:
        print(f"{number} is not a prime number.")
        return

    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break

    if prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

#Task 4
def f4() :
    print("Task4")
    cities = []
    for i in range(1, 6):
        city = input(f"Enter city {i}: ")
        cities.append(city)
    print("Cities you entered:")
    for city in cities:
        print(city)

