class Battery:
    """A simple attempt to model a battery"""
    def __init__(self, battery_size = 75):
        """INitialize the battery's attributes. """
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size} - kWh battery")

class Car:
    """A simple attempt to represent a car"""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formated descriptive name. """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a stattement showing the  car's mileage"""
        print(f"The car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")

    def increment_odometer(self, miles):
        """Add some amount to the odometer reading"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Filling the gas tank"""
        print("Filling the gas tank")


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric car"""
    def __init__(self, make, model, year):
        """ 
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def fill_gas_tank(self):
        """Filling the gas tank"""
        print("This car doesn't need a gas tank!")



