from  numbers import Number

class Point:
    def __init__(self, x: float, y: float):
        if not isinstance(x, Number) or not isinstance(y, Number):
            raise TypeError('Значениями положения точки могут быть только числа')
        else:    
            self.__x = (x)
            self.__y = (y)
    
    def __repr__(self):
        result = [self.__x, self.__y]
        return str(tuple(result))

    def __str__(self):
        return self.__repr__()
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Point):
            if self.x == other.x and self.y == other.y:
                return True
            else:
                return False
        else:
            raise TypeError('Сравнение доступно только для объектов класса Point.')
        
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, numb):
        raise TypeError("'Point' object does not support coordinate assignment")
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, numb):
        raise TypeError("'Point' object does not support coordinate assignment")
    

class Line:

    def __init__(self, start_point: Point, end_point: Point) -> None:
        if self.is_valid(self, start_point) and self.is_valid(self, end_point):
            self.__start = start_point
            self.__end = end_point
        else:
            raise TypeError('Передайте объект класса "Point"')
            
    def __repr__(self):
        res = self.__start.__repr__() + '———' + self.__end.__repr__()
        return res
    def __str__(self):
        return self.__repr__()
    
    @staticmethod
    def is_valid(self, object) -> bool:
        return isinstance(object, Point)


    @property    
    def start(self):
        return(self.__start)
    
    @start.setter
    def start(self, x):
        if self.is_valid(self, x):
            self.__start = x
        else:
            raise TypeError('Передайте значение объекта "Point"')

    @property    
    def end(self):
        return(self.__end)
    
    @end.setter
    def end(self, x):
        if self.is_valid(self, x):
            self.__end = x
        else:
            raise TypeError('Передайте значение объекта "Point"')
    @property
    def length(self):
        res = ((self.__start.x - self.__end.x)**2 + (self.__start.y - self.__end.y)**2)**0.5
        return round(res, 3)

    @length.setter
    def length(self, other):
        raise TypeError("'Line' object does not support length assignment")
    

class Polygon(list):
    def __init__(self, line1: Line,line2: Line,line3: Line, *lines: Line):
        lines += (line1, line2, line3)
        super().__init__(lines)
    
    @staticmethod
    def is_closed(self):
        for i in range(len(self)):
            if i < (len(self) - 1):
                if self[i].end != self[i+1].start:
                    raise TypeError('многоугольник должен быть замкнут')
            elif i == (len(self) - 1):
                if self[i].end != self[0].start:
                    raise TypeError('многоугольник должен быть замкнут')
        return True
    
    @property
    def perimeter(self):
        res = 0
        if self.is_closed(self):
            for lines in self:
                res += lines.length
            return res
    @perimeter.setter
    def perimeter(self, other):
        raise AttributeError("property 'perimeter' of 'Polygon' object has no setter")
        
# ПРОВЕРКА:
# >>> p1 = Point(0, 3)
# >>> p2 = Point(4, 0)
# >>> p3 = Point(8,3)
# >>> p1
# (0, 3)
# >>> repr(p1) == str(p1)
# True
# >>> p1 == Point(0, 3)
# True
# >>> p1 == p2
# False
# >>> p1.x, p2.y
# (0, 0)
# >>> p2.y = 7
# ...
# TypeError: 'Point' object does not support coordinate assignment
# >>> l1 = Line(p1, p2)
# >>> l2 = Line(p2, p3)
# >>> l3 = Line(p3, p1)
# >>> l1
# (0, 3)———(4, 0)
# >>> l1.length
# 5.0
# >>> l3.start = 12
# ...
# TypeError: Передайте значение объекта "Point"
# >>> pol1 = Polygon(l1, l2, l3)
# >>> pol1.perimeter
# 18.0
# >>> pol1.perimeter = 20
# ...
# AttributeError("property 'perimeter' of 'Polygon' object has no setter")
# >>> l3.end = Point(-10,10)
# >>> pol1.perimeter
# ...
# TypeError: многоугольник должен быть замкнут