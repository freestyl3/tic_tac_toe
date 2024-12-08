class Board:
    """Класс, который описывает игровое поле."""

    field_size = 3

    def __init__(self):
        self.board = [[' ' for _ in range(Board.field_size)] for _ in range(Board.field_size)]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * (Board.field_size * 2 - 1))

    def is_board_full(self):
        for i in range(Board.field_size):
            for j in range(Board.field_size):
                if self.board[i][j] == ' ':
                    return False
        return True

    def check_win(self, player):
        # Проверка на победу в строке и в колонке
        for i in range(Board.field_size):
            if (all([self.board[i][j] == player 
                     for j in range(Board.field_size)]) or
                all([self.board[j][i] == player 
                     for j in range(Board.field_size)])):
                return True
        
        # Проверка на победу в диагоналях
        if (all([self.board[i][i] == player 
                 for i in range(Board.field_size)]) or 
            all([self.board[i][Board.field_size - 1 - i] == player 
                 for i in range(Board.field_size)])):
            return True

        return False

    def __str__(self):
        return (
            'Объект игрового поля размером '
            f'{self.field_size}x{self.field_size}'
            )
