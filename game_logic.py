import random

from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Maximum number of mistakes allowed
MAX_MISTAKES = len(STAGES) - 1


def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)


def build_display_word(secret_word, guessed_letters):
    """Return secret word with underscores for unguessed letters."""
    display_letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            display_letters.append(letter)
        else:
            display_letters.append("_")
    return " ".join(display_letters)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the current stage, word progress, and guess summary."""
    print("\n" + "=" * 30)
    print(STAGES[mistakes])
    print(f"Word: {build_display_word(secret_word, guessed_letters)}")
    print(f"Mistakes: {mistakes}/{MAX_MISTAKES}")
    print("=" * 30)


def get_valid_guess(guessed_letters):
    """Prompt until the user enters a new single alphabetical character."""
    while True:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter (a-z).")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
            continue

        return guess


def did_win(secret_word, guessed_letters):
    """Return True if every letter in the secret word has been guessed."""
    return all(letter in guessed_letters for letter in secret_word)


def play_round():
    """Play a single round and return True if won, otherwise False."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("\nWelcome to Snowman Meltdown!")
    print(f"The word has {len(secret_word)} letters.")

    game_won = False

    while mistakes < MAX_MISTAKES and not game_won:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = get_valid_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
            game_won = did_win(secret_word, guessed_letters)
        else:
            mistakes += 1
            print(f"Sorry, '{guess}' is not in the word.")

    # Show final state after a win or a fully melted snowman.
    display_game_state(mistakes, secret_word, guessed_letters)

    if game_won:
        print("Congratulations! You saved the snowman!")
        print(f"The word was: {secret_word}")
    else:
        print("Game Over! The snowman melted away.")
        print(f"The word was: {secret_word}")

    return game_won


def ask_to_play_again():
    """Prompt user to replay and return True for yes, False for no."""
    while True:
        answer = input("Play again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter 'y' or 'n'.")


def play_game():
    """Main entry point; plays rounds until user chooses to stop."""
    while True:
        play_round()
        if not ask_to_play_again():
            print("Thanks for playing Snowman Meltdown!")
            break
