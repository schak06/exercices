#Task 1:
seasons = ("Winter", "Spring", "Summer", "Autumn")

month = int(input("Enter month number (1-12): "))

if month in (12, 1, 2):
    season = seasons[0]
elif month in (3, 4, 5):
    season = seasons[1]
elif month in (6, 7, 8):
    season = seasons[2]
elif month in (9, 10, 11):
    season = seasons[3]
else:
    season = "Invalid month"

print("Season:", season)

#Task 2:
names = set()
while True:
    name = input("Enter a name (empty string to stop): ")
    if name == "":
        break
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("\nNames entered:")
for n in names:
    print(n)

#Task 3:
airports = {}

while True:
    print("\nOptions:")
    print("1 - Enter a new airport")
    print("2 - Fetch airport information")
    print("3 - Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        icao = input("Enter ICAO code: ").upper()
        name = input("Enter airport name: ")
        airports[icao] = name
        print("Airport saved!")

    elif choice == "2":
        icao = input("Enter ICAO code: ").upper()
        if icao in airports:
            print("Airport name:", airports[icao])
        else:
            print("No airport found with that ICAO code.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")