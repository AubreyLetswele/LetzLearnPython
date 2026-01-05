# Inheritence

class Animal:
  def __init__(self, name):
    self.name = name
  def move(self):
    print("Moving")
# Inherits from Animal class
class Dog(Animal):
  # Specific behavior
  def bark(self):
    print("Woof!")
# Creating an instance
my_dog = Dog("Bob")
# Inherited attribute and behavior
print(my_dog.name)
my_dog.move()
# Specific behavior
my_dog.bark()




# Encaapsulation (data hiding)
class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    self.odometer = odometer

  def describe_car(self):
    print(self.year, self.model)

  def read_odometer(self):
    print("Odometer:", self.odometer, "miles")
    
my_car = Car('Audi', 2020, 15000)

my_car.describe_car()
my_car.read_odometer()

#changing a value of the attribute
my_car.odometer = 20000

my_car.read_odometer()



#Polymorphism
class Cat(Animal): # Using your Animal class
    def move(self):
        print("Slinking quietly")

class Dog(Animal):
    def move(self):
        print("Running excitedly")

# Both objects have a .move() method, but they behave differently
animals = [Dog("Bob"), Cat("Whiskers")]

for animal in animals:
    animal.move()
    
    
    

#Abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass # Every shape MUST implement this

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side

# my_shape = Shape() # This would throw an error
my_square = Square(5)
print(f"Square area: {my_square.area()}")