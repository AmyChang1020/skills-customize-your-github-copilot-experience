
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a terminal Hangman game in Python that practices string manipulation, control flow, and handling user input. Students will implement the game loop, word masking, and guess handling.

## 📝 Tasks

### 🛠️ Hangman Game Implementation

#### Description
Implement a playable Hangman game that randomly chooses a secret word and lets the player guess letters until they either reveal the word or run out of attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list included in the repository
- Display the secret word as masked characters (e.g., `_ _ a _ _`)
- Accept single-letter guesses (case-insensitive) and reveal all matching letters
- Prevent and report repeated guesses without penalizing the player
- Track and display remaining incorrect attempts and list of wrong letters
- End the game when the word is fully revealed or attempts are exhausted
- Display a clear win or lose message and reveal the correct word on loss

#### Example gameplay

```
Welcome to Hangman!
Word: _ _ _ _ _
Guess a letter: a
Good guess: _ a _ _ _
Incorrect guesses left: 5
```

#### Starter code
Use the provided `starter-code.py` as a starting point. Run the assignment with:

```bash
python starter-code.py
```

Follow the repository's assignment conventions and keep the README structure consistent with the template.
