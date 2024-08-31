class Game:
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
    
    
    def print_board(self):
        b = self.board
        print(f"""
            A   B   C
        1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
            ----------
        2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
            ----------
        3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)
    

    def print_message(self):
        if not self.tie:
            print("Tie game!")
            if self.winner:
                print(f"{self.winner} wins the game!")
            else:
                print(f"It's player {self.turn}'s turn!")
        else:
            end_message = f"{self.winner}" if self.winner == 'No Winner!' else f"{self.winner} wins the game!"
            print(end_message)

    
    
    
    def render(self):
        self.print_board()
        self.print_message()
    

    def get_move(self):
        move = input(f"Enter a valid move (example: A1): ").lower()
        
        while move not in "a1a2a3b1b2b3c1c2c3" or self.board[move]:
            move = input(f"Invalid input, enter a valid move (example: A1): ").lower()

        self.board[move] = self.turn
        
        return move
    
    def check_winner(self):
        possible_win = [
            self.board['a1'] and (self.board['a1'] == self.board['b1'] == self.board['c1']),
            self.board['a2'] and (self.board['a2'] == self.board['b2'] == self.board['c2']),
            self.board['a3'] and (self.board['a3'] == self.board['b3'] == self.board['c3']),
            self.board['a1'] and (self.board['a1'] == self.board['b2'] == self.board['c3']),
            self.board['a3'] and (self.board['a3'] == self.board['b2'] == self.board['c1']),
            self.board['a1'] and (self.board['a1'] == self.board['a2'] == self.board['a3']),
            self.board['b1'] and (self.board['b1'] == self.board['b2'] == self.board['b3']),
            self.board['c1'] and (self.board['c1'] == self.board['c2'] == self.board['c3'])
        ]

        for win in possible_win:
            if(win):
                self.winner = self.turn
        
        
        return self.winner
    
    def check_for_tie(self):
        for cell in self.board:
            if not self.board[cell]:
                self.tie = False
                return self.tie
        
        self.tie = True

        if not self.winner:
            self.winner = 'No Winner'
        
        return self.tie
    
    
    def switch_turn(self):
        self.turn = 'O' if self.turn == 'X' else 'X'
        return self.turn
    
    def play_game(self):
        print('Welcome to Py-Pac-Poe Game!')

        while not self.tie and not self.winner:
            self.render()
            self.get_move()
            self.check_winner()
            self.check_for_tie()
            self.switch_turn()
    
        self.render()



game_instance = Game()
game_instance.play_game()