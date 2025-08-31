class Task1:
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

class Task2:
    import math
    radius = float(input("Enter your circle radius: "))
    area = (math.pi * radius ** 2)
    print(f"The area is: {area}")

class Task3:
    length = float(input("Enter your rectangle length: "))
    width = float(input("Enter your rectangle width: "))
    perimeter = 2 * (length + width)
    area = (length * width)
    print(f"The perimeter is: {perimeter}")
    print(f"The area is: {area}")

class Task4:
    number1 = int(input("Enter first number:\n "))
    number2 = int(input("Enter second number:\n "))
    number3 = int(input("Enter third number:\n "))
    sum = number1 + number2 + number3
    product = number1 * number2 * number3
    average = (number1 + number2 + number3) / 2
    print(f"The sum is: {sum}")
    print(f"The product is: {product}")
    print(f"The average is: {average}")

class Task5:
    talents = float(input("Enter talents: "))
    pounds = float(input("Enter pounds: "))
    lots = float(input("Enter lots: "))

    grams = (talents * 20 * 32 * 13.3) + (pounds * 32 * 13.3) + (lots * 13.3)

    kilograms = int(grams // 1000)
    grams = grams % 1000

    print(f"The weight in modern units:\n{kilograms} kilograms and {grams:.2f} grams.")

class Task6:
    import random

    # Generate a 3-digit code with numbers between 0 and 9
    digit1 = random.randint(0, 9)
    digit2 = random.randint(0, 9)
    digit3 = random.randint(0, 9)

    # Generate a 4-digit code with numbers between 1 and 6
    dig1 = random.randint(1, 6)
    dig2 = random.randint(1, 6)
    dig3 = random.randint(1, 6)
    dig4 = random.randint(1, 6)

    print(f"3-digit lock code: {digit1}{digit2}{digit3}")
    print(f"4-digit lock code: {dig1}{dig2}{dig3}{dig4}")




