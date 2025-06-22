# Objective: Enhance your understanding of polymorphism in Python by creating a set of classes that 
# demonstrate method overriding and polymorphic behavior.

# Task Description:
# You are tasked with creating a Python script named polymorphism_demo.py. 
# In this script, define a base class Shape with a method area() and derived classes Rectangle and Circle, 
# each overriding the area() method to calculate their respective areas.

# polymorphism_demo.py:
# Base Class - Shape:

# Method: area(self), which simply raises a NotImplementedError, 
# indicating that derived classes need to override this method.
# Derived Class - Rectangle:

# Inherits from Shape.
# Attributes: length and width.
# Overrides the area() method to calculate the rectangle’s area using the formula: length × width.
# Derived Class - Circle:

# Inherits from Shape.
# Attributes: radius.
# Overrides the area() method to calculate the circle’s area using the formula: π × radius² (use math.pi for π).


# Expected Output:
# When you run main.py, the output should reflect the areas of the different shapes, 
# showcasing polymorphism through method overriding.

# The area of the Rectangle is: 50
# The area of the Circle is: 153.


# Note for you:
# Ensure your derived classes Rectangle and Circle correctly override the area method from the Shape base class. 
#     This is key to demonstrating polymorphism.
# The NotImplementedError in the base area method serves as a reminder that this method is 
# expected to be overridden in any subclass of Shape.
# Through this task, you’ll see how different objects can be treated uniformly, 
# yet behave differently based on their respective class implementations—a core concept of polymorphism.

import math
class Shape:
    def area(self):
        """Base method to calculate area, should be overridden in derived classes."""
        raise NotImplementedError("This method should be overridden by subclasses")
class Rectangle(Shape):
    def __init__(self, length, width):
        """Constructor to initialize length and width of the rectangle."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width
class Circle(Shape):
    def __init__(self, radius):
        """Constructor to initialize the radius of the circle."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)
    




