#Task 1
length = float(input("Enter the length of zander (cm): "))

if length < 42:
    print(f"Release the fish! It is {42 - length} cm below the limit.")
else:
    print("Nice catch!")

#Task 2
cabin = input("Enter cabin class (LUX, A, B, C): ").upper()

if cabin == "LUX":
    print("Upper-deck cabin with a balcony.")
elif cabin == "A":
    print("Above the car deck, equipped with a window.")
elif cabin == "B":
    print("Windowless cabin above the car deck.")
elif cabin == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")


#Task 3
gender = input("Enter gender (M/F): ").upper()
hemoglobin = int(input("Enter hemoglobin value: "))

if gender == "F":
    if hemoglobin < 117:
        print("Hemoglobin value is low.")
    elif hemoglobin <= 155:
        print("Hemoglobin value is normal.")
    else:
        print("Hemoglobin value is high.")
elif gender == "M":
    if hemoglobin < 134:
        print("Hemoglobin value is low.")
    elif hemoglobin <= 167:
        print("Hemoglobin value is normal.")
    else:
        print("Hemoglobin value is high.")
else:
    print("Invalid gender.")

#Task 4
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year.")
else:
    print("Not a leap year.")




