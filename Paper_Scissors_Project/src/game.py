    """Author: Emad 
       Describtion: Rock Paper Scissors game.
    """

import random
from typing import List,Tuple


class RockPaperScissor:
    """main class for this game"""
    def __init__(self,name:str):
        self.choices:list[str]= ['rock', 'paper', 'scissors']
        self.player_name:str = name
        
    def get_player_choice(self):    
        user_choice:str = input(f'Enter your choices ({self.choices}): ')
        print(user_choice)
        if user_choice.lower() in self.choices:
            return user_choice.lower()
        
        print(f'Invalid choice, you must select from {self.choices}.')
        return self.get_player_choice()
    
    def get_computer_choice(self):
        """
        :return: PC choice randomly along rock,paper,scissors
        :type: str
        """
        return random.choice(self.choices)
    
    def decide_winner(self, user_choice:str, computer_choice:str)->str:
        """decide winner of the game based on user choices.

        :param user_choice: The choice of user
        :param computer_choice: The choice of computer
        :return: The resukt of the game who is the winner
        """
        if user_choice == computer_choice:
            return ' Its a Tie!'
        
        win_combinations:list[tuple[str,str]] = [('rock','scissors'),('paper', 'rock'),('scissors', 'paper')]
        for win_comb in win_combinations:
            if (user_choice == win_comb[0]) & (computer_choice == win_comb[1]):
                return ' congratulation you won!'

        return 'oh no! the computer won!'
        
    def play(self):
        """play the game.
        _ Get computer choice.
        _ Get computer choice.
        _ Decide the winner.
        _Print the Result
        """
        user_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        print(f'computer_choice: {computer_choice}')
        print(self.decide_winner(user_choice,computer_choice))
        
        
if __name__ == '__main__':
    game = RockPaperScissor('Emad')

while True:
    game.play()
    
    continue_game = input('do you want play again?(Enter any key to play again, enter q to exit!)')
    if continue_game.lower() == 'q':
        break
    
    