# 🎄 Advent of Code - Day 3: Mull It Over 🎄

![Advent of Code Animation](https://user-images.githubusercontent.com/your-gif-link.gif)

## Challenge Description

The North Pole Toboggan Rental Shop's computer memory has been corrupted, and valid multiplication instructions (`mul(X, Y)`) are mixed with invalid characters. The challenge is to identify valid instructions and calculate their results. Additionally, conditional instructions (`do()` and `don't()`) enable or disable future multiplication operations.

---

### Rules

1. **Part 1:**  
   Identify and sum the results of all valid `mul(X, Y)` instructions in the corrupted memory.

2. **Part 2:**  
   Incorporate conditional instructions:
    - `do()`: Enables future `mul` operations.
    - `don't()`: Disables future `mul` operations.  
      Only enabled `mul` operations contribute to the result.

---

### Example

**Part 1:**  
Input:  
`xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))`  
Valid operations:

-   `mul(2,4) → 2 * 4 = 8`
-   `mul(5,5) → 5 * 5 = 25`
-   `mul(11,8) → 11 * 8 = 88`
-   `mul(8,5) → 8 * 5 = 40`  
    **Result:** `8 + 25 + 88 + 40 = 161`

**Part 2:**  
Input:  
`xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))`  
Valid operations:

-   `mul(2,4) → 2 * 4 = 8` (Enabled)
-   `mul(8,5) → 8 * 5 = 40` (Re-enabled after `do()`)  
    **Result:** `8 + 40 = 48`

---

## Results (Based on Input Data)

-   **Part 1 Result:** `170778545`
-   **Part 2 Result:** `82868252`

---

## Learn More

This challenge is part of [Advent of Code](https://adventofcode.com/). Check out the repository for the solution code and input data!
