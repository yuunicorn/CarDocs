"""
Car Documentation
=================

+--------------+
|Cars Available|
+--------------+
|     BMW      |
+--------------+
|   Mercedes   |
+--------------+
|     Lada     |
+--------------+

This module creates a car store that gets items from a car factory.

"""

class Car:
    """
    A single car class.
    All car types inherit from it.

    """
    def __init__(self):
        """
        This is the constructor.

        :param self: The instance of this object.
        :type self: Car

        """
        self.type = ""
        self.model = ""
        self.wheels = 4
        self.doors = 3
        self.seets = 5

    def print_model(self):
        """
        Prints the model of the current car using self.model and self.type.

        :param self: The instance of this object.
        :type self: Car

        :return: Nothing
        :rtype: None
        """
        print("This car is a {model}: {type}, Wow!".format(model=self.model,type= self.type))

    def print_space(self):
        """
        Prints the space in the current car.

        :param self: The instance of this object.
        :type self: Car

        :return: Nothing
        :rtype: None
        """
        print("The car has {0} doors and {1} seets".format(self.doors, self.seets))

    def __str__(self):
        """
        Prints:
        This car is a {s.model}: {s.type}, Wow!
        The car has {s.doors} doors and {s.seets} seets
        :return: A custom string showing the make model and the capacity of current car.
        """
        return """
This car is a {s.model}: {s.type}, Wow!
The car has {s.doors} doors and {s.seets} seets""".format(s=self)


class BMW(Car):
    def __init__(self, **arg):
        """
        Create a BMW class.
        Inherits Car.

        :param arg: Contains information about the BMW car.
        :type arg: dict

        :param type: The type of the car. Should be part of arg. Key is "type".
        :type type: str

        :param doors: The doors that the car has. Should be part of arg. Key is "doors".
        :type doors: int

        :param fuel: The fuel that the car needs. Should be part of arg. Key is "fuel".
        :type fuel: Fuel
        """
        Car.__init__(self)
        self.model = "BMW"
        self.type = "{} Series".format(arg.get("type"))
        self.doors = arg.get("doors")
        self.fuel = arg.get("fuel")

class Mercedes(Car):
    def __init__(self, **arg):
        """
        Create a Mercedes class.
        Inherits Car.

        :param arg: Contains information about the Mercedes car.
        :type arg: dict

        :param type: The type of the car. Should be part of arg. Key is "type".
        :type type: str

        :param doors: The doors that the car has. Should be part of arg. Key is "doors".
        :type doors: int

        :param fuel: The fuel that the car needs. Should be part of arg. Key is "fuel".
        :type fuel: Fuel
        """
        Car.__init__(self)
        self.model = "Mercedes"
        self.type = "{} Class".format(arg.get("type"))
        self.doors = arg.get("doors")
        self.fuel = arg.get("fuel")


class Fuel:
    """

    """
    def __init__(self, **arg):
        """
        The fuel of a car.

        :param arg: The information about the fuel.
        :type arg: dict

        :param liters: How many liters of fuel.
        :type liters: int

        :param type: What type of fuel needed.
        :type type: str
        """
        self.liters = arg.get("liters")
        self.type = arg.get("type")

    def __str__(self):
        """
        Prints:
        It uses {s.liters}L of {s.type}¢.

        :return: A custom string showing what the fuel is.
        """
        return """It uses {s.liters}L of {s.type}¢.""".format(s=self)


class CarFactory:
    def __init__(self, **kwargs):
        self.car = kwargs.get("type")(type=kwargs.get("car_type"),doors=kwargs.get("doors"),fuel=Fuel(liters=kwargs.get("liters"),type=kwargs.get("fuel_type")))

    def get_car(self):
        """Returns a Car"""
        return self.car


class CarStore:
    """
    The car store.
    """
    inventory = []

    def __init__(self, **kwargs):
        self._car_factory = CarFactory(type=kwargs.get("type"), car_type=kwargs.get("car_type"),doors=kwargs.get("doors"),liters=kwargs.get("liters"),fuel_type=kwargs.get("fuel_type"))
        self.inventory.append(self._car_factory.get_car())

    def show_car(self, car=None):
        """
        Shows a car and what fuel it uses.
        If car is not defined, get one from the factory.

        :param car: A car to be displayed. Default: None
        :type car: Car
        :return: Nothing
        :rtype: None
        """
        if not car:
            car = self._car_factory.get_car()

        print(car)
        print(car.fuel)

    def show_inventory(self):
        for i in self.inventory:
            self.show_car(i)

    def __str__(self):
        return "".join([str(i) for i in self.inventory])


store = CarStore(type=Mercedes, car_type= "E", doors=2, liters = 2,fuel_type = "Disel")
store2 = CarStore(type=Mercedes, car_type= "C", doors=4, liters = 2,fuel_type = "Disel")
store3 = CarStore(type=BMW, car_type="1", doors= 3, liters= 2.5, fuel_type = "Gasoline")
store.show_inventory()

print("\n","-"*100)


class Lada(Car):
    def __init__(self, **arg):
        """
        Create a Lada class.
        Inherits Car.

        :param arg: Contains information about the Lada car.
        :type arg: dict

        :param type: The type of the car. Should be part of arg. Key is "type".
        :type type: str

        :param doors: The doors that the car has. Should be part of arg. Key is "doors".
        :type doors: int

        :param fuel: The fuel that the car needs. Should be part of arg. Key is "fuel".
        :type fuel: Fuel
        """
        Car.__init__(self)
        self.model = "Lada"
        self.type = "{}".format(arg.get("type"))
        self.doors = arg.get("doors")
        self.fuel = arg.get("fuel")

store = CarStore(type=Lada, car_type="VAZ-2107",doors=2,liters=1.2,fuel_type="Octane Gasoline")

store.show_inventory()