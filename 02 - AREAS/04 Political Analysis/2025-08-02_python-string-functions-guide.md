---
title: "Python String Functions Guide"
date: 2025-08-02
tags:
  - python
  - creative
  - finance
source: claude-export
---

# Python String Functions Guide

**Date:** 2025-08-02  
**Topics:** [[Python]] · [[Creative]] · [[Finance]]

---

### 🧑 You

give me most used string functions in Python.

---

### 🤖 Claude

Here are the most commonly used string functions and methods in Python:

## Basic String Methods

**len()** - Returns the length of a string
```python
len("hello")  # Returns 5
```

**str()** - Converts other data types to string
```python
str(123)  # Returns "123"
```

## Case Conversion
**upper()** - Converts to uppercase
**lower()** - Converts to lowercase
**capitalize()** - Capitalizes first letter
**title()** - Capitalizes first letter of each word
**swapcase()** - Swaps case of all letters

## Searching and Checking
**find()** - Returns index of substring (or -1 if not found)
**index()** - Like find() but raises exception if not found
**count()** - Counts occurrences of substring
**startswith()** - Checks if string starts with specified prefix
**endswith()** - Checks if string ends with specified suffix
**in** operator - Checks if substring exists

## Splitting and Joining
**split()** - Splits string into list based on delimiter
**join()** - Joins list elements into string with separator
**splitlines()** - Splits on line breaks
**partition()** - Splits into 3 parts around separator

## Replacing and Modifying
**replace()** - Replaces occurrences of substring
**strip()** - Removes whitespace from both ends
**lstrip()** - Removes whitespace from left
**rstrip()** - Removes whitespace from right

## Validation Methods
**isdigit()** - Checks if all characters are digits
**isalpha()** - Checks if all characters are letters
**isalnum()** - Checks if all characters are alphanumeric
**isspace()** - Checks if all characters are whitespace
**islower()** - Checks if all letters are lowercase
**isupper()** - Checks if all letters are uppercase

## Formatting
**format()** - String formatting with placeholders
**f-strings** - Modern string interpolation (f"Hello {name}")
**center()**, **ljust()**, **rjust()** - Text alignment
**zfill()** - Pads with zeros

These cover the vast majority of string manipulation tasks you'll encounter in Python programming.

---
