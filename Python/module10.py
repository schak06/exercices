import random


# Original Car class
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


class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Elevator is now at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}")

    def go_to_floor(self, destination):
        print(f"Moving elevator from floor {self.current_floor} to floor {destination}")
        while self.current_floor < destination:
            self.floor_up()
        while self.current_floor > destination:
            self.floor_down()
        print(f"Elevator has arrived at floor {self.current_floor}")


class Building:
    def __init__(self, bottom, top, num_elevators):
        self.elevators = [Elevator(bottom, top) for _ in range(num_elevators)]
        self.bottom = bottom
        self.top = top

    def run_elevator(self, elevator_number, destination):
        if 1 <= elevator_number <= len(self.elevators):
            print(f"\nRunning elevator {elevator_number} to floor {destination}")
            self.elevators[elevator_number - 1].go_to_floor(destination)
        else:
            print("Invalid elevator number!")

    def fire_alarm(self):
        print("\n Fire alarm! All elevators returning to bottom floor.")
        for i, elevator in enumerate(self.elevators, start=1):
            print(f"Moving elevator {i} to bottom floor...")
            elevator.go_to_floor(self.bottom)

class Race:
    def __init__(self, name, distance_km, cars):
        self.name = name
        self.distance = distance_km
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print(f"\n🏁 Race status: {self.name}")
        print(f"{'Reg.No.':<10}{'Max Speed':<12}{'Current Speed':<15}{'Distance (km)':<15}")
        print("-" * 55)
        for car in self.cars:
            print(f"{car.registration_number:<10}{car.max_speed:<12}{car.current_speed:<15}{car.travelled_distance:<15.1f}")

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)


# Main Program
def main():
    #Elevator test
    print("Elevator Simulation")
    building = Building(bottom=1, top=10, num_elevators=2)
    building.run_elevator(1, 5)
    building.run_elevator(2, 8)
    building.fire_alarm()

    #Race test
    print("\nGrand Demolition Derby")
    cars = [Car(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]
    race = Race("Grand Demolition Derby", 8000, cars)

    hour = 0
    while not race.race_finished():
        hour += 1
        race.hour_passes()
        if hour % 10 == 0:
            race.print_status()

    print(f"\n Race finished in {hour} hours!")
    race.print_status()


if __name__ == "__main__":
    main()
