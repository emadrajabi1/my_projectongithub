# Decimal to Hex Converter

A Python program that converts a decimal (base 10) number to its hexadecimal (base 16) equivalent using a manual algorithm.

## Description

* Enter a decimal number
* The program converts it to hexadecimal
* Conversion is implemented manually (no `hex()` usage)
* Press ENTER to exit

## Features

* Decimal → Hexadecimal conversion
* Input validation (handles invalid input)
* Supports zero correctly
* Loop for multiple conversions
* Clean formatted output

## Requirements

* Python +3.7

## Project Structure
```
Dec_To_Hex/
│
└── src/
    │
    └── dec_to_hex/
        │
        ├── hex.py # the main project
        └── README.md     # this file

```

## How to Run

```
python hex.py
```

## How It Works

* Takes user input
* Validates numeric input
* Repeatedly divides the number by 16
* Stores remainders
* Maps values:

  * 10 → A
  * 11 → B
  * 12 → C
  * 13 → D
  * 14 → E
  * 15 → F
* Reverses the result to get final hexadecimal

## Example

```id="q2m7dn"
Enter a decimal number: 255
Hexadecimal: FF

Enter a decimal number: 16
Hexadecimal: 10
```

## Author
Emad

