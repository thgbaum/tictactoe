import random


class TicTacToe:

    def __init__(self):
        self.player = ''
        self.player_points = 0
        self.computer_points = 0
        self.ties = 0
        self.matches = 0
        self.display_instructions()
        self.select_X_or_O()

    
    def score(self):
        print('MATCHES: ', self.matches)
        print('Computer: ', self.computer_points)
        print('Player: ', self.player_points)
        print('Ties: ', self.ties)


    def display_instructions(self):
        self.filler = f'{"-" * 30 }'

        print(f"""
        {2*self.filler}

                  ▀█▀ █ ▄▀▀   ▀█▀ ▄▀▄ ▄▀▀   ▀█▀ ▄▀▄ ██▀
                   █  █ ▀▄▄    █  █▀█ ▀▄▄    █  ▀▄▀ █▄▄

                   
        {self.filler[0:-7]} Instructions {self.filler[0:-7]}
            when making a move choose    Filling order                              
            from 1-9 in order to fill       1|2|3
            the gaps and win the game       4|5|6
                    Good Luck!              7|8|9
        {2*self.filler}
            """)
        

    def select_X_or_O(self):
        player=''
        while player not in ['o', 'O', 'x', 'X']:
            player = str(input("Do you want to play as 'O' or 'X' ?? "))

        if player in ['o', 'O']:
            self.computer = ' X '
            self.player = ' O '

        elif player in ['x', 'X']:
            self.computer = ' O '
            self.player = ' X '
   

    def set_game(self):
        self.s1 = '(1)'
        self.s2 = '(2)'
        self.s3 = '(3)'
        self.s4 = '(4)'
        self.s5 = '(5)'
        self.s6 = '(6)'
        self.s7 = '(7)'
        self.s8 = '(8)'
        self.s9 = '(9)'
        self.possible_moves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.s_correlation = ['',self.s1, self.s2, self.s3, self.s4, self.s5, self.s6, self.s7, self.s8, self.s9]
        self.match_over = False
        self.matches +=1


    def update_game(self):
        self.s1 = self.s_correlation[1]
        self.s2 = self.s_correlation[2]
        self.s3 = self.s_correlation[3]
        self.s4 = self.s_correlation[4]
        self.s5 = self.s_correlation[5]
        self.s6 = self.s_correlation[6]
        self.s7 = self.s_correlation[7]
        self.s8 = self.s_correlation[8]
        self.s9 = self.s_correlation[9]
        game = f" \
    \n   {self.s1} | {self.s2} | {self.s3} \
    \n -------------------\
    \n   {self.s4} | {self.s5} | {self.s6} \
    \n -------------------\
    \n   {self.s7} | {self.s8} | {self.s9} \
    \n"
        print(game)


    def make_a_move(self, player_, choice, symbol):
        if player_ == 'computer':
            choice = random.choice(self.possible_moves)

        self.possible_moves.remove(choice)
        self.s_correlation[int(choice)] = symbol 


    def play_game(self):
        
        choice = ''
        turn = random.choice([0,1])
        move = ''   

        while self.match_over == False:
            if turn == 0:
                move = 'computer'
                self.make_a_move(move, choice, self.computer)
                turn = 1
                print(move)

            elif turn == 1:
                while choice not in self.possible_moves:
                    choice = str(input('What\'s your next move)? '))
                    if choice in self.possible_moves:
                        ...
                    elif choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        print('Slot already taken, try again!')
                    else:
                        print('Only numbers from 1 to 9 allowed, try again')

                move = 'player'
                self.make_a_move(move, choice, self.player)
                turn = 0
                print(move)

            self.update_game()

            if (self.s1 == self.s2 == self.s3) or \
            (self.s4 == self.s5 == self.s6) or \
            (self.s7 == self.s8 == self.s9) or \
            (self.s1 == self.s4 == self.s7) or \
            (self.s2 == self.s5 == self.s8) or \
            (self.s3 == self.s6 == self.s9) or \
            (self.s1 == self.s5 == self.s9) or \
            (self.s3 == self.s5 == self.s7):
                
                self.match_over = True
                print(f'{move.upper()} wins this match\n')
                if move == 'computer':
                    self.computer_points+=1
                    

                if move == 'player':
                    self.player_points+=1

                self.score()

            elif self.possible_moves == []:
                self.match_over = True
                print('Tie\n')
                self.ties +=1
                self.score()
        
        
    def run_match(self):
        self.set_game()
        self.update_game()
        self.play_game()
    

    def main(self):
        self.run_match()
        self.rematch = ''
        while self.rematch not in ['y', 'Y', 'n', 'N']:
            self.rematch = input('Keep playing? (Y)es or (N)o ')
            print(self.rematch)
        self.rematch_()


    def rematch_(self):
        if self.rematch in ['y', 'Y']:
            self.main()   
        
        else:
            print(2*self.filler)
            self.score()
            if self.player_points > self.computer_points:
                print('PLAYER wins!')
            elif self.computer_points > self.player_points:
                print('COMPUTER wins!')
            elif self.computer_points == self.player_points:
                print('TIE GAME!')


TicTacToe().main()
        