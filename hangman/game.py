from .exceptions import *

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['testing','project', 'functionaliy','oops', 'borked']


def _get_random_word(list_of_words):
    pass


def _mask_word(word):
    if len(word) < 1:
        raise InvalidWordException ("Invalid word used!")
    
    masked_word = ''
    for letters in word:
        print(letters)
        masked_word += '*'
    return masked_word


def _uncover_word(answer_word, masked_word, character):
    pass


def guess_letter(game, letter):
    pass


def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game
