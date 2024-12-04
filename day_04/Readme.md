# 🎄 Advent of Code - Day 4: Ceres Search 🎄

![Advent of Code Animation](https://user-images.githubusercontent.com/your-gif-link.gif)

## Challenge Description

While searching for the Chief at the Ceres monitoring station, an Elf requests your help with her word search puzzle. The goal is to find occurrences of specific patterns in the grid.

---

### Rules

1. **Part 1:**  
   Find all instances of the word `XMAS`.

    - Words can appear horizontally, vertically, diagonally, backwards, or overlapping.

    Example:

    MMMSXXMASM <br/>
    MSAMXMSMSA <br/>
    AMXSXMAAMM <br/>
    MSAMASMSMX <br/>
    XMASAMXAMM <br/>
    XXAMMXXAMA <br/>
    SMSMSASXSS <br/>
    SAXAMASAAA <br/>
    MAMMMXMMMM <br/>
    MXMXAXMASX

In this example, `XMAS` appears **18 times**.

2. **Part 2:**  
   Find all instances of an **X-MAS** pattern, where two `MAS` form an `X`.

-   Each `MAS` can be written forwards or backwards.
-   An example pattern:
    ```
    M.S
    .A.
    M.S
    ```

Example:

MMMS...... <br/>
.SAM.MSMS. <br/>
M.M.M.AA.. <br/>
.SAMASMSM. <br/>
M.M.M..... <br/>
.......... <br/>
S.S.S.S.S. <br/>
A.A.A.A... <br/>
M.M.M.M.M. <br/>
.......... 

In this example, an X-MAS pattern appears **9 times**.

---

## Results (Based on Input Data)

-   **Part 1 Result:** `2583` (Occurrences of `XMAS`)
-   **Part 2 Result:** `1978` (Occurrences of `X-MAS` pattern)

---

## Learn More

This challenge is part of [Advent of Code](https://adventofcode.com/). Check out the repository for the solution code and input data!
