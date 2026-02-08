class Queen:
    def __init__(self, row, column):
        self.row = row
        self.column = column

        if self.row < 0:
            raise ValueError("row not positive")
        if self.row > 7:
            raise ValueError("row not on board")
        if self.column < 0:
            raise ValueError("column not positive")
        if self.column > 7:
            raise ValueError("column not on board")
    def can_attack(self, another_queen):
        self.another_queen = another_queen

        if self.another_queen.column == self.column and self.row == self.another_queen.row:
            raise ValueError("Invalid queen position: both queens in the same square")
        if abs(self.column - self.another_queen.column) == abs(self.row - self.another_queen.row):
            return True
        return (self.column == self.another_queen.column) or (self.another_queen.row == self.row)