# Challange: Write a python function to determine the probability of certian outcomes when rolling dice
# Using Monte Carlo Method
# Input: variable number of arguments for sides of dice
# Output: table of proability for each possible outcome

import random

def roll_dice(times,dice1,dice2,dice3):
    N = times
    
    # prepare hit results
    maximum_result = dice1 + dice2 + dice3
    dice_hit_reults = {}
    for i in range(maximum_result):
        # create key
        hit_number = i + 1
        hit_number_str = str(hit_number)
        key = "hit_" + hit_number_str
        dice_hit_reults[key] = 0

    for i in range(N):
        roll_dice1 = random.randint(1,dice1)
        roll_dice2 = random.randint(1,dice2)
        roll_dice3 = random.randint(1,dice3)

        dice_result = roll_dice1 + roll_dice2 + roll_dice3

        # Count on each result
        for i in range(maximum_result):
            hit_number = i + 1
            hit_number_str = str(hit_number)
            key = "hit_" + hit_number_str
            if dice_result == hit_number:
                dice_hit_reults[key] += 1
    # Summary proability by each result
    for i in range(maximum_result):
        hit_number = i + 1
        hit_number_str = str(hit_number)
        key = "hit_" + hit_number_str

        outcome = 100 * dice_hit_reults[key] / times

        # print("out come probability for 1 = ",outcome)
        print(f"out come probability for {hit_number} = {outcome}")


roll_dice(1000000,4,6,6)

        