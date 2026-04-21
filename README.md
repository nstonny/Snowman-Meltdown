# Snowman Meltdown

A terminal word-guessing game inspired by hangman.

You guess one letter at a time to reveal the secret word before the snowman fully melts.
Each wrong guess advances the melting ASCII art stage.

## Project Structure

- `snowman.py` - Entry point that starts the game.
- `game_logic.py` - Core game flow, input validation, and replay logic.
- `ascii_art.py` - Snowman melt stages used during gameplay.

## Requirements

- Python 3.8+ (or newer)

## How to Run

```bash
cd /Users/nayeema/Masterschool/Term2/Week4/Project/Snowman-Meltdown
python snowman.py
```

## How the Game Works

- A random word is selected from a small built-in word list.
- You can only enter one alphabetical character per guess.
- Repeated guesses are rejected.
- Correct guesses reveal matching letters in the word.
- Incorrect guesses increase the mistake counter and melt the snowman.
- You win by revealing every letter before reaching the final melt stage.
- After each round, you can choose to play again.

## Future Improvements

- Add more words and categories.
- Add difficulty levels (easy/medium/hard).
- Track score across multiple rounds.
- Save high scores to a file.

