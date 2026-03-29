from Courier import Courier
class CarCourier(Courier):
    car_model: str
    fuel: float
    fuel_consumption: float
    def __init__(self, name, experience, rating, completed_orders, balance, is_busy, car_model, fuel, fuel_consumption):
        super().__init__(name, experience, rating, completed_orders, balance, is_busy)
        self.car_model = car_model
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
    def print_info(self):
        super().print_info()
        print(f"Car Model: {self.car_model}")
        print(f"Fuel: {self.fuel} liters")
        print(f"Fuel Consumption: {self.fuel_consumption} liters/km")
    def deliver_order(self, distance: float):
        required_fuel = distance * self.fuel_consumption
        if self.fuel < required_fuel:
            raise NotImplementedError("Not enough fuel to deliver the order.")
        else:
            self.completed_orders += 1
            self.fuel -= required_fuel
            self.calculate_salary_for_order(distance)
            self.print_info()
    def calculate_salary_for_order(self, distance: float):
        self.balance += 200 + (distance*40)
    def refuel(self, liters: float):
        if liters <= 0:
            raise NotImplementedError("Fuel amount must be greater than zero.")
        else:
            self.fuel += liters
            print(f"Refueled {liters} liters. Current fuel {self.fuel} liters.")
            self.print_info()
