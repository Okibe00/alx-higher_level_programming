#!/usr/bin/python3
'''
Module creates a Rectangle class that inherits from Base
'''
from models.base import Base


class Rectangle(Base):
    '''
    Rectangle class
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
            initialization method
        '''

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @classmethod
    def integer_validator(self, name, value):
        '''
            validates user input
        '''
        if type(value) == bool:
            raise TypeError(f"{name} must be an integer")

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if name in "xy":
            if value < 0:
                raise ValueError(f"{name} must be >= 0")

        if value <= 0 and name not in 'xy':
            raise ValueError(f"{name} must be > 0")

        return value

    def __str__(self):
        '''
        print string representation of Rectangle
        '''
        return f"[{self.__class__.__name__}] ({self.id})\
                {self.x}/{self.y} - {self.width} / {self.height}"

    def display(self):
        '''
            prints a rectangle
        '''
        for i in range(self.__height):
            if i == 0:
                print("\n" * self.__y, end="")
            format_str = " " * self.__x + "#" * self.__width
            print(format_str)

    def area(self):
        return self.__width * self.__height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, width):
        self.__width = self.integer_validator("width", width)

    @height.setter
    def height(self, height):
        self.__height = self.integer_validator("height", height)

    @x.setter
    def x(self, x):
        self.__x = self.integer_validator("x", x)

    @y.setter
    def y(self, y):
        self.__y = self.integer_validator("y", y)
