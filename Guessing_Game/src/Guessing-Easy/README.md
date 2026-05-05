# Guessing Number Game

A simple Python game where the computer selects a random number and the user tries to guess it.

## Features

* Random number generation
* Input validation with error handling
* Range checking
* Hint system (higher / lower)
* Continuous loop until correct guess

## Game Structure

```
Guessing_Game/
│
└── src/
    │
    └── Guessing_Easy/
        │
        ├── guessing.py   # the main game
        └── README.md     # this file
```

## Requirements

* Python +3.7

## How to Run

```
python guessing.py
```

## How It Works

* The computer selects a random number
* User enters guesses
* If input is invalid → error message
* If number is out of range → warning
* If guess is lower → hint: bigger
* If guess is higher → hint: lower
* Game ends when the correct number is guessed

## Example

```id="8k3djn"
tell me your guess: 50
Help: number is Bigger
tell me your guess: 75
Help: number is Lower
tell me your guess: 63
you're Hit the number, Correct!
```

## Author
Emad
