import random

def number_guessing_game():
    print("\n=== NUMBER GUESSING GAME ===")
    print("I'm thinking of a number between 1 and 100")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
        attempts += 1      
        if guess == secret_number:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    else:
        print(f"\n😞 Game Over! The number was {secret_number}")

number_guessing_game()
