# Example 4 - Guessing Game - Correct Solution

import random

num = random.randrange(1, 101)
guess = int(input("Guess a number between 1-100: "))

while guess != num:
  if guess > num:
    print ("Too high")
  else:
    print ("Too low")
  guess = int(input("Guess again: "))

print ("Congratulations")