class Courier:
    name: str
    experiance: int
    rating: float
    completed_orders: int
    balance: float
    is_busy: bool
    
    def __init__(self, name: str, experiance: int, rating: float, completed_orders: int, balance: float, is_busy: bool):
        self.name = name
        self.experiance = experiance
        self.rating = rating
        self.completed_orders = completed_orders
        self.balance = balance
        self.is_busy = is_busy
    
    def print_info(self):
        print(f'Name: {self.name}')
        print(f'Experience: {self.experiance} years')
        print(f'Rating: {self.rating}')
        print(f'Completed Orders: {self.completed_orders}')
        print(f'Balance: {self.balance}')
        print(f'Is Busy: {self.is_busy}')
    
    def deliver_order(self, distance: float):
        if distance <= 0:
            raise NotImplementedError('Distance must be greater than zero.')
        else:
            self.distance = distance
    
    def finish_shift(self):
        self.is_busy = False
        print(f'{self.completed_orders} order completed. Balance: {self.balance}. Shift finished.')
