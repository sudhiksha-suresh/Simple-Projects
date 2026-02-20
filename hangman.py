import random

def play_hangman():
    # Predefined list of 5 words
    words = ["python", "programming", "developer", "hangman", "coding"]
    
    # Select random word
    secret_word = random.choice(words).upper()
    guessed_word = ["_"] * len(secret_word)
    incorrect_guesses = 0
    max_incorrect = 6
    guessed_letters = set()
    
    print("=" * 50)
    print("🎯 WELCOME TO HANGMAN!")
    print("=" * 50)
    print(f"Try to guess the word. It has {len(secret_word)} letters.")
    print(f"You have {max_incorrect} incorrect guesses allowed.")
    print("-" * 50)
    
    while incorrect_guesses < max_incorrect and "_" in guessed_word:
        # Display current game state
        print(f"\nWord: {' '.join(guessed_word)}")
        print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect}")
        print(f"Letters guessed: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        
        # Get player input
        guess = input("\nEnter a letter: ").upper().strip()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter!")
            continue
        
        if guess in guessed_letters:
            print("❌ You already guessed that letter!")
            continue
        
        # Add to guessed letters
        guessed_letters.add(guess)
        
        # Check if guess is correct
        if guess in secret_word:
            print(f"✅ Good guess! '{guess}' is in the word!")
            
            # Update the guessed word
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            incorrect_guesses += 1
            print(f"❌ Wrong! '{guess}' is not in the word.")
            print(f"💀 Hangman progress: {incorrect_guesses}/{max_incorrect}")
    
    # Game over - check result
    print("\n" + "=" * 50)
    
    if "_" not in guessed_word:
        print("🎉 CONGRATULATIONS! YOU WON!")
        print(f"The word was: {secret_word}")
        print("You guessed it with", max_incorrect - incorrect_guesses, "guesses remaining!")
    else:
        print("💀 GAME OVER! You ran out of guesses.")
        print(f"The word was: {secret_word}")
    
    print("=" * 50)

def main():
    while True:
        play_hangman()
        
        # Ask if player wants to play again
        play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
        if play_again not in ['y', 'yes']:
            print("Thanks for playing! Goodbye!")
            break
        print("\n" + "=" * 50)

if __name__ == "__main__":
    main()
