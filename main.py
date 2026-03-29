from BikeCourier import BikeCourier
from CarCourier import CarCourier
from FootCourier import FootCourier


delivery1 = BikeCourier("John", 5, 4.5, 100, 5000, False, "Mountain Bike", 80)
delivery2 = CarCourier("Alice", 10, 4.8, 200, 15000, False, "Toyota Camry", 50, 0.1)
delivery3 = FootCourier("Bob", 3, 4.2, 50, 2000, False, 5, 10)

delivery1.print_info()
delivery2.print_info()
delivery3.print_info()

def give_order(courier, distance):
    try:
        courier.deliver_order(distance)
    except NotImplementedError:
        print("Not enough fuel to deliver the order.")
give_order(delivery1, 3)
give_order(delivery2, 400)
give_order(delivery3, 4)

def print_rules_and_formulas(couriers, sample_distance: float):
    print("Restrictions And Salary Formulas")
    print("===============================")
    print("1. Foot Courier:")
    print("   - Maximum distance: 5 km")
    print("   - Salary formula: 120 + (distance * 25)")
    print("2. Bike Courier:")
    print("   - Stamina decreases by 10 for each order")
    print("   - Salary formula: 150 + (distance * 30)")
    print("3. Car Courier:")
    print("   - Fuel consumption: 0.1 liters/km")
    print("   - Salary formula: 200 + (distance * 40)")
    print("Sample Salary Calculations:")
    print("==============================")