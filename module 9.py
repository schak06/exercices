import random

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

#Main Program

car = Car("ABC-123", 142)
print("Initial car properties:")
print(f"Registration number: {car.registration_number}")
print(f"Maximum speed: {car.max_speed} km/h")
print(f"Current speed: {car.current_speed} km/h")
print(f"Travelled distance: {car.travelled_distance} km")
print()


car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(f"Speed after accelerations: {car.current_speed} km/h")


car.accelerate(-200)
print(f"Speed after emergency brake: {car.current_speed} km/h")
print()


car.current_speed = 60
car.drive(1.5)
print(f"Travelled distance after driving 1.5 hours at 60 km/h: {car.travelled_distance} km")
print()

#Car Race Simulation
cars = []
for i in range(1, 11):
    max_speed = random.randint(100, 200)
    registration = f"ABC-{i}"
    cars.append(Car(registration, max_speed))

race_finished = False
hour = 0

while not race_finished:
    hour += 1
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)
        if car.travelled_distance >= 10000:
            race_finished = True
            break

print(f"\nRace finished in {hour} hours!\n")
print(f"{'Reg.No.':<10}{'Max Speed':<12}{'Current Speed':<15}{'Distance (km)':<15}")
print("-" * 55)
for car in cars:
    print(f"{car.registration_number:<10}{car.max_speed:<12}{car.current_speed:<15}{car.travelled_distance:<15.1f}")
