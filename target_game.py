"""
Target game
"""
import random
import string
from typing import List

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    counter = 0
    letters = []
    grid = []
    while counter != 9:
        grid.append(random.choice(string.ascii_letters).upper())
        counter += 1
        if len(grid) == 3:
            letters.append(grid)
            grid = []
    return letters    


def get_words(file: str, letters: List[str]) -> List[str]:
    """
    Reads the file file. Checks the words with rules and returns a list of words.
    """


def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter 
    for Windows.
    Note: the user presses the enter key after entering each word.
    """


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    >>> get_pure_user_words(['ham', 'apple', 'pepe', 'loop', 'lopj', 'orange', 'lope'], \
    ['a', 'l' 'e', 'p', 'p', 'o', 'o', 'j', 'e'], \
    ['apple', 'pepe', 'loop', 'ham', 'orange'])
    ['lopj', 'lope']
    """

def results():
    """
    Writting result in file
    """

