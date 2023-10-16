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

    def to_dictionary(self):
        '''
        returns dictionary representation
        '''
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}

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

    def update(self, *args, **kwargs):
        if len(args) != 0 and isinstance(args[0], int):
            for i, v in enumerate(args):
                if i == 0:
                    self.id = self.integer_validator("id", v)
                elif i == 1:
                    self.width = v
                elif i == 2:
                    self.height = v
                elif i == 3:
                    self.x = v
                elif i == 4:
                    self.y = v
        else:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = self.integer_validator("id", v)
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def __str__(self):
        '''
        print string representation of Rectangle
        '''
        return (f"[{self.__class__.__name__}] ({self.id})" +
                f" {self.x}/{self.y} - {self.width}/{self.height}")

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
