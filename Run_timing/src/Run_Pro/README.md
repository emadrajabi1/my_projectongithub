# Run Timing Advanced (Run Pro)

A Python program to track and analyze running sessions with detailed statistics.

## Description

* Enter running distances (in kilometers)
* Press ENTER to stop input
* The program computes summary statistics

## Features

* Multiple run input support
* Input validation (no negatives, no invalid values)
* Calculates:

  * Total runs
  * Average distance
  * Fastest run (min)
  * Slowest run (max)
* Uses `statistics` module
* Structured output

## Requirements

* Python 3.x

## Game Structure
```
|
|--str/
    |--run.py-the main game
|
|--README.md - This file

```

## How to Run

```
python run.py
```

## How It Works

* Distances are collected in a list
* Invalid inputs are rejected
* Statistics are computed:

  * `mean()` for average
  * `min()` for fastest
  * `max()` for slowest
* Results are printed with separators

## Example

```id="q7v2bn"
Enter distance (KM): 5
Enter distance (KM): 8.2
Enter distance (KM): 6
Enter distance (KM):

Runs: [5.0, 8.2, 6.0]
Total runs: 3
--------------------------------------------------
Average: 6.4 KM
Fastest run: 5.0 KM
Slowest run: 8.2 KM
```

## Author

Emad
