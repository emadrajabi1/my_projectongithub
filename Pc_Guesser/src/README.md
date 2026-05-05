# PC Guesser - Number Guessing Game (Reverse)

A Python game where the computer guesses the number you are thinking of using binary search.

## Description

* Think of a number between 1 and 1000
* The computer will try to guess it
* After each guess, respond with:

  * `c` → Correct
  * `b` → Bigger
  * `s` → Smaller


## Game Structure

```
|
|--scr/
    |--guesser.py-the main game
|
|--README.md - This file

```
## Features

* Efficient guessing using binary search
* Minimal number of attempts
* Simple interactive input
* Deterministic narrowing of range

## Requirements

* Python +3.7

## How to Run

```
python guesser.py
```

## How It Works

* Initial range is set from 1 to 1000
* The computer always guesses the middle of the range
* Based on your feedback:

  * `b` → range shifts upward
  * `s` → range shifts downward
  * `c` → game ends
  * ` enter` → break
* Process repeats until the correct number is found

## Example

```id="y7r2hx"
Is it 500? (c/b/s): b
Is it 750? (c/b/s): s
Is it 625? (c/b/s): c
```

## Author
Emad
