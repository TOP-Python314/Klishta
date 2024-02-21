class ChessKing:
    files = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
    ranks = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8}
    def __init__(self, color = 'white'):
        self.color = color
        if self.color == 'white':
            self.square ='e1'
        elif self.color == 'black':
            self.square = 'e8'
        else:
            raise TypeError
    def __repr__(self):
            return f'{self.get_name()}: {self.square}'
    def __str__(self):
            return f'{self.get_name()}: {self.square}'
    def get_name(self):
        for name, values in globals().items():
            if values is self:
                return name

    def is_turn_valid(self, check):
            if check[0] in ChessKing.files and check[1] in ChessKing.ranks:
                if (ChessKing.files[check[0]] - 1 <= ChessKing.files[self.square[0]] <= ChessKing.files[check[0]] + 1)  and (ChessKing.ranks[check[1]] - 1 <= ChessKing.ranks[self.square[1]] <= ChessKing.ranks[check[1]] +1):
                    return True
                else:
                     return False
            else:
                raise TypeError
    def turn(self, check):
            if check[0] in ChessKing.files and check[1] in ChessKing.ranks:
                if (ChessKing.files[check[0]] - 1 <= ChessKing.files[self.square[0]] <= ChessKing.files[check[0]] + 1)  and (ChessKing.ranks[check[1]] - 1 <= ChessKing.ranks[self.square[1]] <= ChessKing.ranks[check[1]] +1):
                    self.square = check
                else:
                     raise ValueError
            else:
                raise TypeError
                
# ПРОВЕРКА:
# >>> wk = ChessKing()
# >>> wk.color
# 'white'
# >>> wk.square
# 'e1'
# >>> wk
# wk: e1
# >>> wk.is_turn_valid('f2')
# True
# >>> wk.is_turn_valid('a2')
# False
# >>> bk = ChessKing('black')
# >>> bk.color
# 'black'
# >>> bk.square
# 'e8'
# >>> bk.turn('d7')
# >>> bk.square
# 'd7'
# >>> print(bk)
# bk: d7
# >>> bk.turn('a2')
# ValueError