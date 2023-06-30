import random
import re

def getWordList():
  with open('words.txt', 'r') as f:
    return f.read().strip().split('\n')

class colors:
  @classmethod
  def green(cls, text):
    return f'\033[32m{text}\033[0m'

  @classmethod
  def yellow(cls, text):
    return f'\033[93m{text}\033[0m'

  @classmethod
  def red(cls, text):
    return f'\033[31m{text}\033[0m'

def getNewAnswer(word_list):
  return random.choice(word_list)

def getGuess(word_list):
  resp = ''
  while not re.match('^[a-z]{5}$', resp) or resp not in word_list:
    resp = input('Guess: ').lower()
  return resp

def getFormattedDisplay(answer, guess):
  remaining_map = {}
  for i in range(0, len(answer)):
    if answer[i] == guess[i]:
      continue
    c = answer[i]
    remaining_map[c] = remaining_map.get(c, 0) + 1

  result = ''
  for i in range(0, len(answer)):
    if answer[i] == guess[i]:
      result += colors.green(guess[i])
    elif remaining_map.get(guess[i], 0) > 0:
      result += colors.yellow(guess[i])
      remaining_map[guess[i]] -= 1
    else:
      result += colors.red(guess[i])
  return result

def checkGuess(answer, guess):
  display = guess
  display = getFormattedDisplay(answer, guess)
  return (answer == guess, display)

def play():
  word_list = getWordList()
  answer = getNewAnswer(word_list)
  max_tries = 5
  tries = 0
  while True:
    guess = getGuess(word_list)
    tries += 1
    correct, display = checkGuess(answer, guess)
    print(display)
    if correct:
      print('You won!')
      return True
    if tries == max_tries:
      print('Game Over')
      print(f'Answer: {answer}')
      return False

play()
