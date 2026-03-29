from Courier import Courier
class FootCourier(Courier):
    max_distance: float
    speed: float
    def __init__(self, name, experience, rating, completed_orders, balance, is_busy, max_distance, speed):
        super().__init__(name, experience, rating, completed_orders, balance, is_busy)
        self.max_distance = max_distance
        self.speed = speed
    def print_info(self):
        super().print_info()
        print(f"Max Distance: {self.max_distance} km")
        print(f"Speed: {self.speed} km/h")
    def deliver_order(self, distance: float):
        if self.is_busy:
            raise NotImplementedError("Courier is already busy.")
        else:
            if distance > self.max_distance:
                raise NotImplementedError("Distane exceeds maximum limit for foot courier.")
            else:
                self.completed_orders += 1
                self.calculate_salary_for_order(distance)
                self.is_busy = True
                self.print_info()     
    def calculate_salary_for_order(self, distance: float):
        self.balance += 120 + (distance*25)
