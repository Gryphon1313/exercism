class Queen:
    def __init__(self, row: int, column: int):
        if row < 0:
            raise ValueError("row not positive")
        if column < 0:
            raise ValueError("column not positive")
        if row > 7:
            raise ValueError("row not on board")
        if column > 7:
            raise ValueError("column not on board")
        self.row = row
        self.column = column

    def can_attack(self, another_queen: 'Queen') -> bool:
        if not isinstance(another_queen, Queen):
            raise TypeError("Another queen must be an instance of the Queen class")
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        return (
            self.row == another_queen.row or
            self.column == another_queen.column or
            abs(self.row - another_queen.row) == abs(self.column - another_queen.column)
        )
