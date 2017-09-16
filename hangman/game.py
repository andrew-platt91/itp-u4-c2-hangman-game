from .exceptions import *
from random import randint

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['testing','project', 'functionaliy','oops', 'borked']

#This is Complete and Passing all tests\|/\|/
def _get_random_word(list_of_words):
    try:
        random_word = list_of_words[randint(0,len(list_of_words)-1)]
    except:
        raise invalidlistofwordseexception('invalid List of words')

    return random_word

def _mask_word(word):
    if len(word) < 1:
        raise InvalidWordException ("Invalid word used!")
    
    masked_word = ''
    for letters in word:
        print(letters)
        masked_word += '*'
    return masked_word


def _uncover_word(answer_word, masked_word, character):
    # Raise an exception if character length not equal to 1
    if len(character) != 1:
        raise InvalidGuessedLetterException ('Invalid character Guessed')
    # Raise an exceptoin if answer_word is blank or if answer word and masked word length don't match
    if len(answer_word) < 1 or len(answer_word) != len(masked_word):
        raise InvalidWordException('Invalid word used!')
    #  Make a list out of the masked word so we can choose were to 
    word_unmasked = list(masked_word) 
    # get all Positons of the letter using list comprehension and enumerate
    unmask_location = [index for index, letter in enumerate(answer_word.lower()) if letter == character.lower()]
    # unmask characters found in unmasked_location through their location
    for location in unmask_location:
        word_unmasked[location] = character.lower()
    # Join the list of unmasked words together
    return ''.join(word_unmasked)
    
def guess_letter(game, letter):
    #Ok This is big one. from what i can tell it needs to take the guessed letter
    #compare it to the list of answer word
    #if it finds the letter in the answer word it needs to modify the masked word
    #if it fails to find i.e. None it needs to run the Miss exception 
    #it needs to drop the number of guesses down if it the Miss exception is raised
    #although we mabe able to incorparate that into a miss exception function
    #regardless of all that it needs to append the guess to the 
    
    #lets start by breaking the two words into a list for comparison
    answer_word_to_list = list(game['answer_word'])
    masked_word_to_list = list(game['masked_word'])
    # for each letter in the list let is the letter in the list
    for individual_letters in answer_word_to_list:
        indices = []
        if individual_letters == letter:
            
            uncover_word(game['answer_word'], game['masked_word'], letter)
        else:
            game['remaining_misses'] = game['remaining_misses']-1
            game['previous_guesses'].append(letter)
    
    return game

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
