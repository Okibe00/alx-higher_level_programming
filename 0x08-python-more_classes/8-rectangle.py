#!/usr/bin/python3
'''modules creates a class'''


class Rectangle:
    '''
        class variables
    '''
    number_of_instances = 0
    print_symbol = "#"

    '''creates an empty class'''
    def __init__(self, width=0, height=0):
        '''
        initilizes instance of class
        args:
            width: width
            height: height
        '''
        self.x = ""
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
                print(str(self.print_symbol) * self.__width)
            else:
                return str(self.print_symbol) * self.__width

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''
            compares objects
        '''
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2
