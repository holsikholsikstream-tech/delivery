from Courier import Courier
class BikeCourier(Courier):
    bike_type: str
    stamina: int
    def __init__(self, name, experience, rating, completed_orders, balance, is_busy, bike_type, stamina):
        super().__init__(name, experience, rating, completed_orders, balance, is_busy)
        self.bike_type = bike_type
        self.stamina = stamina
    def print_info(self):
        super().print_info()
        print(f"Bike Type: {self.bike_type}")
        print(f"Stamina: {self.stamina}")
    def deliver_order(self, distance: float):
        if self.stamina <= 0:
            raise NotImplementedError("Courier is to tired to deliver the order.")
        else:
            self.completed_orders += 1
            self.stamina -= 10
            self.calculate_salary_for_order(distance)
            self.print_info()
    def calculate_salary_for_order(self, distance: float):
        self.balance += 150 + (distance*30)
