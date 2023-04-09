import math
import random
import numpy as np
from io import StringIO
countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
populations = [5615000, 5439000, 324000, 5080000, 9609000]
male_fishers = [1822, 2575, 3400, 11291, 1731]
female_fishers = [69, 77, 400, 320, 26]

def guess(winner_gender):
    all_fishers = 0
    if winner_gender == 'female':
        fishers = female_fishers
        for each in fishers:
            all_fishers += each
    else:
        fishers = male_fishers
        for each in fishers:
            all_fishers += each

    guess = None
    biggest = 0.0

    for i in range(len(fishers)):
        if fishers[i]/all_fishers > biggest:
            guess = countries[i]
            biggest = fishers[i]/all_fishers
        else:
            continue
    return (guess, biggest*100)  

def main():
    country, fraction = guess("male")
    print("if the winner is male, my guess is he's from %s; probability %.2f%%" % (country, fraction))
    country, fraction = guess("female")
    print("if the winner is female, my guess is she's from %s; probability %.2f%%" % (country, fraction))

main()

  