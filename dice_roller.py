import random

def main():

    # Set the number of dice to roll
    dice_rolls = 2

    # Create a variable to store the sum of the dice
    dice_sum = 0

    # Roll the dice and sum them
    for i in range(0, dice_rolls):
        roll = random.randint(1, 6)
        dice_sum += roll
        print(f'You rolled a {roll}')
    print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
    main()
