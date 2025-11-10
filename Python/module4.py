#Task 1
n = 1
while n <= 1000:
    if n % 3 == 0:
        print(n)
    n += 1
#Task 2
while True:
    inches = float(input("Enter inches (negative to quit): "))
    if inches < 0:
        break
    print(f"{inches} inches = {inches * 2.54:.2f} cm")
#Task 3
number_str = input("Enter a number (empty input stops): ")

if number_str == "":
    print("No numbers entered.")
else:
    number = float(number_str)
    smallest = number
    largest = number

    while number_str != "":
        number = float(number_str)
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number
        number_str = input("Enter a number (empty input stops): ")

    print(f"Smallest number: {smallest}")
    print(f"Largest number: {largest}")
#Task 4
import random
secret = random.randint(1, 10)

guess = int(input("Guess the number (1–10): "))
while guess != secret:
    if guess < secret:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Guess the number (1–10): "))
print("Correct!")

#Task 5
username = "py"
password = "1234"

attempts = 0
user = input("Username: ")
pw = input("Password: ")

while (user != username or pw != password) and attempts < 4:
    print("Wrong credentials")
    attempts = attempts + 1
    user = input("Username: ")
    pw = input("Password: ")

if user == username and pw == password:
    print("Welcome")
else:
    print("Access denied")
#Task 6
import random

rounds = int(input("How many random points to generate: "))
inside = 0
done = 0

while done < rounds:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        inside = inside + 1
    done = done + 1

pi_estimate = 4 * inside / rounds
print(f"Approximation of pi: {pi_estimate:.5f}")
