class Queen:
    def __init__(self, row, column):
        self.row = row
        self.column = column

        for name, value in [('row', self.row), ('column', self.column)]:
            if value < 0:
                raise ValueError(f'{name} not positive')
            if value > 7:
                raise ValueError(f'{name} not on board')

    def can_attack(self, another_queen):
        if another_queen.column == self.column and self.row == another_queen.row:
            raise ValueError("Invalid queen position: both queens in the same square")
        return abs(self.column - another_queen.column) == abs(self.row - another_queen.row) or self.column == another_queen.column or another_queen.row == self.row