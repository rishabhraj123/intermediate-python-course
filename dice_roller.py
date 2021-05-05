import random

def main():

  dice_rolls = 2
  print(f'You rolled {dice_rolls} dice(s)')
  dice_sum = 0
  for i in range(dice_rolls):
  	roll = random.randint(1,6)
  	print(f'You rolled a {roll}')
  	dice_sum += roll

  print(f'You rolled a total of {dice_sum}')

if __name__== "__main__":
  main()