import random  

def new_game():
    print("Welcome to the new game!")
    play = input("Do you want to play 'Guess the Number'? (yes/no): ").lower()
    if play == 'yes':
        guess_the_number()
    else:
        print("Maybe next time! Bye!")

def guess_the_number():
    name = input("Hello! What is your name?\n")  
    number = random.randint(1, 20)  
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    attempts = 0  
    
    while True:
        try:
            guess = int(input("Take a guess.\n"))  
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1  
        if guess < number:
            print("\nYour guess is too low.")
        elif guess > number:
            print("\nYour guess is too high.")
        else:
            print(f"\nGood job, {name}! You guessed my number in {attempts} guesses!")
            break


new_game()
