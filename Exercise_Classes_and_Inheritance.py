class Animal:

    """Animal"""

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print("Getting Name")
        return self.__name

    @name.setter
    def name(self, new_name):
        print("Setting Name")
        self.__name = new_name

    def move(self):
        print('Moving')


class Fish(Animal):
    """Fish Class, inheriting from Animal"""
    def __init__(self, name,size):
        super().__init__(name)
        self.__size = size
    
    @property
    def size(self):
        print("Getting size")
        return self.__size

    @size.setter
    def size(self, new_size):
        print("Setting Size")
        self.__size = new_size


class Snake(Animal):
    """Snake Class, inheriting from Animal"""
    def __init__(self, name,length):
        super().__init__(name)
        self.__length = length
    
    #G and S

class Person(Animal):
    """Person Class, inheriting from Animal"""
    def __init__(self, name,height):
        super().__init__(name)
        self.__height = height
    
    #G and S



class Book:
    def __init__(self,title):
        self.__title = title

    @property
    def title(self):
        print("Getting title")
        return self.__title

    @title.setter
    def title(self, new_title):
        print("Setting title")
        self.__title = new_title

    def collectingdust(self):
        print('Collecting Dust')


class textbook(Book):
    """textbook Class, inheriting from Book"""
    def __init__(self, name,topic):
        super().__init__(name)
        self.__topic = topic

    #G and S

class addressbook(Book):
    """addressbook Class, inheriting from Book"""
    def __init__(self, name,pages):
        super().__init__(name)
        self.__pages = pages
        
    #G and S


class Vehicle:
    def __init__(self,Brand):
        self.__Brand = Brand

    @property
    def brand(self):
        print("Getting brand")
        return self.__brand

    @brand.setter
    def title(self, new_brand):
        print("Setting brand")
        self.__brand = new_brand

    def Skkrrt(self):
        print('Skkrrtt')


class Car(Vehicle):
    """Car Class, inheriting from Vehicle"""
    def __init__(self, name,doors):
        super().__init__(name)
        self.__pages = pages
        
    #G and S

class Bicycle(Vehicle):
    """Bicycle Class, inheriting from Vehicle"""
    def __init__(self, name,tires):
        super().__init__(name)
        self.__tires = tires
        
    #G and S

class Boat(Vehicle):
    """Boat Class, inheriting from Vehicle"""
    def __init__(self, name,sails):
        super().__init__(name)
        self.__sails = sails
        
    #G and S

class Hot_air_Balloon(Vehicle):
    """Hot air balloon Class, inheriting from Vehicle"""
    def __init__(self, name,size):
        super().__init__(name)
        self.__size = size
        
    #G and S