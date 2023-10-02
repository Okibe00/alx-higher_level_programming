#!/usr/bin/python3
'''modules creates a class'''


class Rectangle:
    '''
    creates a rectangle
    class variables:
    number_of_instances
    '''
    number_of_instances = 0
    '''creates an empty class'''
    def __init__(self, width=0, height=0):
        '''
        initilizes instance of class
        args:
            width: width
            height: height
        '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''
            gets value of width
        '''
        return self.__width

    @width.setter
    def width(self, width):
        '''
        sets value of width
        args:
            width: width value
        '''
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        '''
        gets value of height
        '''
        return self.__height

    @height.setter
    def height(self, height):
        '''
        sets value of height
        args:
            height: height value
        '''
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def area(self):
        '''
            returns area of rectangle
        '''
        return self.__height * self.__width

    def perimeter(self):
        '''
            return perimter of rectangle
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width * 2 + self.__height * 2

    def __str__(self):
        '''
        return string
        '''
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            for i in range(self.__height - 1):
                print("#" * self.__width)
            else:
                return "#" * self.__width

    def __repr__(self):
        '''
        returns string representation of class
        '''
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        '''
        delete an instance
        '''
        Rectangle.number_of_instances -= 1
        print(f"Bye rectangle" + str("..."))
