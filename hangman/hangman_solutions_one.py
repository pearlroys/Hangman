
from os import name
import random



class Hangman:
     
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, name, word_list, num_lives=6, x=0):

        self.name = input('Pls enter your name: ')
        print(f"Hello {self.name}, welcome to the medical hangman. This is a game where a random anatomical part in your boay is presented \
            and you will have 6 tries to guess the part or you lose it. Good luck!")
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        print(f"The mystery word has {len(self.word)} characters")
        self.word_guessed = []
        for letters in (self.word):
            self.word_guessed.append("_")
        print(self.word_guessed)
        self.num_letter = len(set(self.word))
        self.list_letters = []
        self.x = x
    
    def hangman_picture(self, x):
            self.x = x
            

            if x == 1: 
                  print('''
    +---+
    O   |
   /|\  |
   / \  |
       ===''')
                  print('\n you lose a leg')
 
    

            elif x == 2:
                  print('''
    +---+
    O   |
   /|\  |
   /    |
       ===''')
                  print('\n you lose another leg')

            elif x == 3:
                  print('''
    +---+
    O   |
   /|\  |
        |
       ===''')
                  print('\n you lose an arm')

            elif x == 4:
                  print('''
    +---+
    O   |
   /|   |
        |
       ===''')
                  print('\n you lose another arm')

            elif x == 5:
                  print('''
    +---+
    O   |
    |   |
        |
       ===''')
                  print('\n you lose your gut')

            elif x == 6:
                  print('''
     +---+
    O   |
        |
        |
       ===''')
                  print('\n you lose your head. You suck!')


       
    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''  
        
        self.list_letters.append(letter)
        for i, l in enumerate(self.word):
            if letter.lower() == l:
                self.word_guessed[i] = l
                self.num_letter -= 1
                print(f"Nice! {letter} is in the word!")
                print("".join(self.word_guessed))
                    
            elif letter not in self.word:
                print(f"Sorry, {letter} is not in the word. You lose a part!")
                self.list_letters.append(letter)
                self.x += 1
                self.hangman_picture(self.x)
                self.num_lives -= 1
                print(f' You have {self.num_lives} lives left')
                break
                    
        
            if '_' not in self.word_guessed:
                print("Congratulations, you won")
                
            
        

            if self.num_lives == 0:
                print(f'You ran out of lives. The word was {self.word}')
            
    

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        while True:
            letter = input("Enter a single letter: ")
            if len(letter) > 1:
                print("Please, enter just one character")
            elif letter.isalpha() is False:
                print('Only alphabets please')
            elif letter in self.list_letters:
                print(f"{letter} was already tried, choose again")
            elif len(letter) == 1:
                break
                
            else:
                print('Please, enter a character')

        return letter

def play_game(word_list):
    # As an aid, part of the code is already provided:
    game = Hangman(name, word_list, num_lives=6)
    while game.num_lives > 0 and '_' in game.word_guessed:
        letter = game.ask_letter()
        game.check_letter(letter)
    


if __name__ == '__main__':
    word_list = ['skull', 'humerus', 'femur', 'mandible', 'clavicle','duodenum']
    play_game(word_list)


# %%
