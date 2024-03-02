from numbers import Number


class Matrix:
    def __init__(self, *rows: tuple, n: int = 0, m: int = 0):
        self.__rows = rows
        self.n = n #кол-во строк
        self.m = m #кол-во столбцов
        if not self.is_valid(self.__rows, self.n, self.m):
            raise ValueError('невозможно сконструировать матрицу')
    
    @staticmethod
    def is_valid(item: tuple | Number, n, m) -> bool:
        for thing in item:
            if not isinstance(thing, Number):
                return False
            if len(item) != n * m:
                return False
        return True
    
    def __repr__(self):
        result =""
        rows = list(self.__rows)
        str___rows = [len(str(num)) for num in rows]
        for i in range(self.n):
            max_len_digit = max(str___rows)
            for j in range(self.m):
                result += str(rows[i*self.m + j]).rjust(max_len_digit)
                if j == 0:
                    max_len_digit += 1
            max_len_digit = max(str___rows)
            result += '\n'
            
        return result
    
    @property
    def transpose(self):
        rows = list(self.__rows)
        rows_test =[]
        for i in range(self.m):
            test = rows[i::self.m]
            rows_test.extend(test)
        
        return Matrix(*rows_test,n=self.m,m=self.n)

    # def __getitem__(self, key):
    #     return self.__rows[key]
        
    def __element_wise_operation(self, other, sign):
        result = []
        if isinstance(other, Matrix) or isinstance(other, Number):
            match sign:
                case '+':
                    if isinstance(other, Matrix):   
                        if self.n == other.n and self.m == other.m:
                            for i in range(len(self.__rows)):
                                result.append(self.__rows[i] + other.__rows[i])
                               
                        else:
                            raise TypeError('матрицы должны иметь одинаковый размер')
                    else:
                        for i in range(len(self.__rows)):
                            result.append(self.__rows[i] + other)
                    return result
                case '-':
                    if isinstance(other, Matrix):   
                        if self.n == other.n and self.m == other.m:
                            for i in range(len(self.__rows)):
                                result.append(self.__rows[i] - other.__rows[i])
                               
                        else:
                            raise TypeError('матрицы должны иметь одинаковый размер')
                    else:
                        for i in range(len(self.__rows)):
                            result.append(self.__rows[i] - other)
                    return result
                case '1-':
                    if isinstance(other, Matrix):   
                        if self.n == other.n and self.m == other.m:
                            for i in range(len(self.__rows)):
                                result.append(other.__rows[i] - self.__rows[i])
                               
                        else:
                            raise TypeError('матрицы должны иметь одинаковый размер')
                    else:
                        for i in range(len(self.__rows)):
                            result.append(other - self.__rows[i])
                    return result
                case '*':
                    if isinstance(other, Matrix):   
                        raise NotImplementedError('умножение матриц будет реализовано в будущем')

                    else:
                        for i in range(len(self.__rows)):
                            result.append(other * self.__rows[i])
                    return result
        else:
            raise TypeError('алгебраические операции возможны только с матрицами и числами')
    def __add__(self, other):
        res = self.__element_wise_operation(other, '+')
        return Matrix(*res, n=self.n, m=self.m)
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        res = self.__element_wise_operation(other, '-')
        return Matrix(*res, n=self.n, m=self.m)
    
    def __rsub__(self, other):
        res = self.__element_wise_operation(other, '1-')
        return Matrix(*res, n=self.n, m=self.m)
    def __neg__(self):
        res = []
        for digit in self.__rows:
            res.append(-digit)
        return Matrix(*res,n=self.n,m=self.m)
    def __mul__(self, other):
        res = self.__element_wise_operation(other, '*')
        return Matrix(*res,m=self.m, n=self.n)
    def __rmul__(self, other):
        return self.__mul__(other)
    
m1 = Matrix(1,2,3,4,5,6,n=2,m=3)


# ПРОВЕРКА:
# >>> m1
# 1 2 3
# 4 5 6

# >>> m1.transpose
# 1 4
# 2 5
# 3 6

# >>> m1*m1
# ...
# NotImplementedError: умножение матриц будет реализовано в будущем
# >>> m1*3
#  3  6  9
# 12 15 18

# >>> 3*m1
#  3  6  9
# 12 15 18

# >>> m1-3
# -2 -1  0
#  1  2  3

# >>> 3-m1
#  2  1  0
# -1 -2 -3

# >>> m1
# 1 2 3
# 4 5 6

# >>> m1+10
# 11 12 13
# 14 15 16

# >>> 10-m1
# 9 8 7
# 6 5 4

# >>> m2 = Matrix(1,1,1,1,1,1,m=3,n=2)
# >>> m2
# 1 1 1
# 1 1 1

# >>> m2 = Matrix(1,1,1,'a',1,1,m=3,n=2)
# ...
# ValueError: невозможно сконструировать матрицу
# >>> m2 = Matrix(1,1,1,1,m=2,n=2)
# >>> m2
# 1 1
# 1 1

# >>> m1
# 1 2 3
# 4 5 6

# >>> m1+m2
# ...
# TypeError: матрицы должны иметь одинаковый размер
# >>> m1*m2
# ...
# NotImplementedError: умножение матриц будет реализовано в будущем