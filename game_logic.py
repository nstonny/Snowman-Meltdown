import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Maximum number of mistakes allowed
MAX_MISTAKES = len(STAGES) - 1


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the current game state: snowman stage and word progress."""
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])

    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    #print("Guessed letters:", ", ".join(guessed_letters) if guessed_letters else "None")
    print()


def play_game():
    """Main game loop for Snowman Meltdown."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    game_won = False

    print("Welcome to Snowman Meltdown!")
    print(f"The word has {len(secret_word)} letters.\n")

    # Game loop - continue until win or lose
    while mistakes <= MAX_MISTAKES:
        # Display current game state
        display_game_state(mistakes, secret_word, guessed_letters)

        # Prompt user for a guess
        guess = input("Guess a letter: ").lower()

        # Validate input
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.\n")
            continue

        # Check if letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter!\n")
            continue

        # Add guess to list
        guessed_letters.append(guess)

        # Check if guess is correct
        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.\n")
        else:
            print(f"Sorry, '{guess}' is not in the word.\n")
            mistakes += 1

        # Check if player won
        if all(letter in guessed_letters for letter in secret_word):
            game_won = True
            break

        # Check if player lost
        if mistakes > MAX_MISTAKES:
            break

    # Display final game state (cap mistakes at MAX_MISTAKES for display)
    display_mistakes = min(mistakes, MAX_MISTAKES)
    print(STAGES[display_mistakes])

    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print()

    # Display end game message
    if game_won:
        print("🎉 Congratulations! You saved the snowman! 🎉")
        print(f"The word was: {secret_word}")
    else:
        print("❌ Game Over! The snowman has melted away...")
        print(f"The word was: {secret_word}")


