# PERMUTATIONS WITHOUT DUPLICATES
import random

def n_factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n * n_factorial(n-1)

def permutations(word):
    combinations_number = n_factorial(len(word))
    set_1 = set()
    list_chars = list(word) # list of chars
    
    while len(set_1) != combinations_number:
        random.shuffle(list_chars) # make combination
        set_1.add(''.join(list_chars)) # add combination string to set
    
    return list(set_1)

print("\nWellcome to Permutations App!")

is_running = True
while is_running:
    word = input("\nEnter a word: ") 

    if len(word) == 0:
        print("\n   You must enter a word...")

    elif any(char.isspace() for char in word):
        print("\n   You must provide only a word without blanks...")

    else:
        result = permutations(word) 
        for i, combination in enumerate(result):
            print(f"\tCombination {i+1}:", combination)
        is_running = False

print("\nThanks! See on")

