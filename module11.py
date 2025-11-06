
#Task1: Publications
class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book: {self.name}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.page_count}\n")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine: {self.name}")
        print(f"Chief Editor: {self.chief_editor}\n")


# Task 2:

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume



#Main
def main():

    print("=== Publications ===")
    magazine = Magazine("Donald Duck", "Aki Hyyppä")
    book = Book("Compartment No. 6", "Rosa Liksom", 192)

    magazine.print_information()
    book.print_information()

    print("=== Cars ===")
    e_car = ElectricCar("ABC-15", 180, 52.5)
    g_car = GasolineCar("ACD-123", 165, 32.3)

    e_car.accelerate(120)
    g_car.accelerate(100)

    e_car.drive(3)
    g_car.drive(3)

    print(f"Electric car {e_car.registration_number} distance: {e_car.travelled_distance} km")
    print(f"Gasoline car {g_car.registration_number} distance: {g_car.travelled_distance} km")


if __name__ == "__main__":
    main()
