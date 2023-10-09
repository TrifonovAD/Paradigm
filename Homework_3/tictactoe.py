class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'  # Начинает игрок X

# Вывести текущее состояние доски
    def print_board(self):
        for row in [self.board[i:i + 3] for i in range(0, 9, 3)]:
            print('| ' + ' | '.join(row) + ' |')
            print('-------------')

    def make_move(self, position):
        if 0 < position < 10 and self.board[position - 1] == ' ':
            self.board[position - 1] = self.current_player
            return True
        return False

# Проверка есть ли победитель в игре
    def is_winner(self, player):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False
   
# Проверить, заполнена ли доска
    def is_board_full(self):
        return ' ' not in self.board

# Переключение игрока
    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def play_game(self):
        print("Добро пожаловать в игру Крестики-нолики!")
        while True:
            self.print_board()
            position = int(input(f"Игрок {self.current_player}, выберите позицию (1-9): "))
            if self.make_move(position):
                if self.is_winner(self.current_player):
                    self.print_board()
                    print(f"Поздравляем! Игрок {self.current_player} победил!")
                    break
                elif self.is_board_full():
                    self.print_board()
                    print("Ничья!")
                    break
                else:
                    self.switch_player()
            else:
                print("Неверный ход.")


if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()