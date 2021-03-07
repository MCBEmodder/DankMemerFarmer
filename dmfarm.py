import pynput
import time
import random
from pynput import keyboard
from time import sleep
from random import randint
from pynput.keyboard import Key, Controller, Listener

#For pls pm
postmeme = ["f", "r", "i", "c", "k"]

#For pls trivia
trivia = ["a", "b", "c", "d"]

#For Pls hl
hl = ["high", "low", "jackpot"]

#You can freely edit them but you must have 3-4 words in there to avoid being detected instantly by dankmemer
words = ["I regret nothing", "dm farm bot", "hmmm", "what if I do this"]

keyboard = Controller()

i = 0
time.sleep(10)

while i < 1:
  
    keyboard.type('/dm beg')
    time.sleep(0.3)
    keyboard.press(Key.enter)
    time.sleep(2)
    
    keyboard.type('/dm hunt')
    time.sleep(0.3)
    keyboard.press(Key.enter)
    time.sleep(4)

    keyboard.type(random.choice(words))
    time.sleep(2)
    keyboard.press(Key.enter)
    
    keyboard.type('/dm fish')
    time.sleep(0.3)
    keyboard.press(Key.enter)
    time.sleep(2)

    keyboard.type(random.choice(words))
    time.sleep(2)
    keyboard.press(Key.enter)

    keyboard.type('/dm pm')
    time.sleep(0.3)
    keyboard.press(Key.enter)
    time.sleep(2)
    
    keyboard.type('/dm hl')
    time.sleep(0.3)
    keyboard.press(Key.enter)
    time.sleep(2)
    
    keyboard.type(random.choice(hl))
    time.sleep(0.3)
    keyboard.press(Key.enter)
    time.sleep(2)
    
    keyboard.type('/dm dep max')
    time.sleep(0.3)
    keyboard.press(Key.enter)
    time.sleep(2)

    keyboard.type('Cycle done')
    time.sleep(0.3)
    keyboard.press(Key.enter)
    time.sleep(2)
    
    keyboard.type(random.choice(postmeme))
    keyboard.press(Key.enter)
    time.sleep(38)

    
