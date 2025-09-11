import random
import math

#Task 1
def roll_dice():
    return random.randint(1, 6)

def f1():
    print("Rolling until we get 6...")
    num = roll_dice()
    print(num)
    while num != 6:
        num = roll_dice()
        print(num)


#Task2
def roll_dice_sides(sides):
    return random.randint(1, sides)

def f2():
    sides = int(input("Enter number of sides on the dice: "))
    print(f"Rolling until we get {sides}...")
    num = roll_dice_sides(sides)
    print(num)
    while num != sides:
        num = roll_dice_sides(sides)
        print(num)


#Task3
def gallons_to_litres(gallons):
    return gallons * 3.78541

def f3():
    gallons = float(input("Enter volume in gallons (negative to stop): "))
    while gallons >= 0:
        litres = gallons_to_litres(gallons)
        print(f"{gallons} gallons = {litres:.2f} litres")
        gallons = float(input("Enter volume in gallons (negative to stop): "))


#Task 4
def sum_list(numbers):
    return sum(numbers)

def f4():
    numbers = [1, 2, 3, 4, 5]
    print("Numbers:", numbers)
    print("Sum =", sum_list(numbers))


#Task 5
def remove_odds(numbers):
    return [n for n in numbers if n % 2 == 0]

def f5():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    print("Original list:", numbers)
    evens = remove_odds(numbers)
    print("Without odd numbers:", evens)


#Task6
def pizza_unit_price(diameter, price):
    radius = diameter / 2
    area_cm2 = math.pi * radius * radius
    area_m2 = area_cm2 / 10000  # convert cm² to m²
    return price / area_m2

def f6():
    print("Pizza 1:")
    d1 = float(input("Enter diameter (cm): "))
    p1 = float(input("Enter price (€): "))

    print("Pizza 2:")
    d2 = float(input("Enter diameter (cm): "))
    p2 = float(input("Enter price (€): "))

    v1 = pizza_unit_price(d1, p1)
    v2 = pizza_unit_price(d2, p2)

    print(f"Pizza 1 unit price: {v1:.2f} €/m²")
    print(f"Pizza 2 unit price: {v2:.2f} €/m²")

    if v1 < v2:
        print("Pizza 1 is better value for money!")
    else:
        print("Pizza 2 is better value for money!")


# Run tasks
if __name__ == "__main__":
    print("Task 1:")
    f1()
    print("\nTask 2:")
    f2()
    print("\nTask 3:")
    f3()
    print("\nTask 4:")
    f4()
    print("\nTask 5:")
    f5()
    print("\nTask 6:")
    f6()
