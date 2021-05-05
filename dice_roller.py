import random

def main():
	dice_rolls = int(input("How many Dice would you like to roll? > "))
	dice_size = int(input("How many sides does the dice have? > "))
	print(f'You rolled {dice_rolls} dice(s)')
	dice_sum = 0

	for i in range(dice_rolls):
		roll = random.randint(1,dice_size)

		if roll == 1:
			print(f'You rolled a {roll}! Critical Fail')
		elif roll == dice_size:
			print(f'You rolled a {roll}! Critical Success!')
		else:
			print(f'You rolled a {roll}')

		dice_sum += roll

	print(f'You rolled a total of {dice_sum}')

if __name__== "__main__":
  main()