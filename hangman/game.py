from hangman.exceptions import *
import random
# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
  try: 
      word= random.choice(list_of_words)
      return word 
  except:
    raise InvalidListOfWordsException


def _mask_word(word):
  if word == '':
    raise InvalidWordException
  masked_word = masked_word = '*'* len(word)
  return masked_word


def _uncover_word(answer_word, masked_word, character):
  current_masked = answer_word
  # conditions to raise exception. 
  if len(answer_word) != len(masked_word) or answer_word == '': 
    raise InvalidWordException
  if len(character) != 1:
    raise InvalidGuessedLetterException   
    
  for char in answer_word: 
    # cater for case insentive case 
    # only mask those unrevealed answer
    if char.lower() != character.lower() and char.lower() not in masked_word.lower():
        current_masked = current_masked.replace(char, '*')
  masked_word = current_masked.lower()
  return masked_word



def guess_letter(game, letter): 
  if '*' not in game['masked_word'] or game['remaining_misses'] == 0:
    raise GameFinishedException
    
  game['masked_word'] =  _uncover_word(game['answer_word'],game['masked_word'], letter)
  game['previous_guesses'].append(letter.lower())
  if letter.lower() not in game['answer_word'].lower():
    game['remaining_misses'] = game['remaining_misses'] -1 
  if '*' not in game['masked_word']:
    raise GameWonException
  if game['remaining_misses'] == 0:
    if '*' not in game['masked_word']:
      raise GameWonException
    else: 
      raise GameLostException
    
  
    

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
