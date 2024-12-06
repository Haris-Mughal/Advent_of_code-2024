# 🎄 Advent of Code - Day 2: Red-Nosed Reports 🎄

![Advent of Code Animation](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOTlhaHE5OGgxdHQwOG1pMjBreGNoNnJzbDB6cDQ2a25iYWg0eHgxdSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3W2uhnQap3Nza/giphy.gif)

## Challenge Description

Analyze reactor safety reports to determine if they are safe based on the following rules:

1. **Part 1:** Reports are safe if:
    - Levels are strictly increasing or decreasing.
    - Adjacent level differences are between 1 and 3.
2. **Part 2:** With the **Problem Dampener**, a single level can be ignored to make a report safe.

---

### Example

**Part 1:**

-   `7 6 4 2 1`: **Safe** (levels decrease by 1 or 2).
-   `1 2 7 8 9`: **Unsafe** (difference of 5 between levels).

**Part 2:**

-   `8 6 4 4 1`: **Safe** (removing `4` makes levels valid).
-   `1 3 2 4 5`: **Safe** (removing `3` makes levels valid).

---

## Results (Based on Input Data)

-   **Part 1 Safe Reports:** `411`
-   **Part 2 Safe Reports:** `465`

---

## Learn More

This challenge is part of [Advent of Code](https://adventofcode.com/). Check out the repository for code and input data!
