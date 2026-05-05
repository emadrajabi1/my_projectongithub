# Guessing Number Game (Professional)

A fun Python guessing game where the computer picks a random number and you try to guess it within limited attempts.

## Features

* Three difficulty levels: Easy, Medium, Hard
* Different ranges and attempt limits for each level
* Random number generation
* Input validation with error handling
* Range checking
* Helpful hints (Too high / Too low)
* Score calculation based on performance
* Play again option

## Requirements

* Python +3.7

## Game Structure

```
Guessing_Game/
│
└── src/
    │
    └── Guessing_Pro/
        │
        ├── guessing.py   # the main game
        └── README.md     # this file

```

## How to Run

```
python guessing.py
```

## Difficulty Levels

| Level  | Range    | Attempts  |
| ------ | -------  | --------  |
| Easy   | 0 - 100  |    5      |
| Medium | 0 - 500  |    7      |
| Hard   | 0 - 1000 |   10      |

## How It Works

* Select a difficulty level
* The system generates a random number
* Enter your guesses within the allowed attempts
* Receive hints after each guess
* Game ends when:

  * You guess correctly
  * Attempts run out

## Example

```
Select difficulty (easy/medium/hard): medium
Guess the number: 40
Too low
Guess the number: 75
Too high
Guess the number: 60
Correct! You guessed the number.
Score: 80
```

## Author
Emad
