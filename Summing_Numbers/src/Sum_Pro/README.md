# Summing Numbers (Professional)

A Python program that collects numbers from the user and provides detailed statistics.

## Description

* Enter numbers one by one
* Press ENTER to stop input
* The program calculates total, count, average, largest, and smallest values

## Features

* Continuous input loop
* Input validation with error handling
* Tracks:

  * Total sum
  * Count of numbers
  * Average
  * Largest number
  * Smallest number
* Handles empty input safely

## Requirements

* Python +3.7

## Project Structure

```
Summing_Numbers/
│
└── src/
    │
    └── Sum_Pro/
        │
        ├── sum.py   # the main game
        └── README.md     # this file
```

## How to Run

```
python sum.py
```

## How It Works

* Initializes:

  * `total`, `count`
  * `largest`, `smallest`
* Reads user input in a loop
* Converts valid input to integer
* Updates statistics dynamically
* Stops when input is empty
* Prints final results

## Example

```id="r8n3vl"
enter number: 10
enter number: 5
enter number: 20
enter number:

Total: 35
Count: 3
Average: 11.66
Largest: 20
Smallest: 5
```

## Author
Emad
