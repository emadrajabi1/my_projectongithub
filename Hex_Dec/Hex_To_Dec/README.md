# Hex to Decimal Converter

A Python program that converts a hexadecimal (base 16) number to its decimal (base 10) equivalent using a manual algorithm.

## Description

* Enter a hexadecimal value (e.g. `FF`, `1A3`)
* The program converts it to decimal
* Supports uppercase and lowercase input
* Press ENTER to exit

## Features

* Hex → Decimal conversion
* Case-insensitive input (`A-F` / `a-f`)
* Input validation for invalid characters
* Manual conversion using base-16 logic
* Loop for multiple conversions

## Requirements

* Python +3.7

## Game Structure
```
|
|--scr/
    |--dec.py-the main game
|
|--README.md - This file

```

## How to Run

```
python dec.py
```

## How It Works

* Reads input as string
* Validates characters (0–9, A–F)
* Processes digits from right to left
* Converts each digit:

  * `A–F` → `10–15`
* Multiplies by powers of 16
* Sums all values to get final decimal

## Example

```id="m6q9vx"
Enter hex number: FF
Decimal: 255

Enter hex number: 1A3
Decimal: 419
```

## Author
Emad
