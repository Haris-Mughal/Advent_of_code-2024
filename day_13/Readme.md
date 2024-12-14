# Advent of Code - Day 13: Claw Contraption 🎮

![Claw Machine Animation](https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif)

## Challenge Description

The resort's claw machines work in an unusual way, requiring you to strategically press buttons to align the claw with prizes. Each button moves the claw differently, and tokens have varying costs for each button press.

---

### Rules

1. **Part 1:**  
   Calculate the minimum tokens required to win as many prizes as possible, using given claw movements and prize positions.

2. **Part 2:**  
   Adjust prize positions and recalculate the minimum token cost for winning the maximum number of prizes.

---

### Example

**Part 1:**  
Input:

-   Button A: `X+94, Y+34`
-   Button B: `X+22, Y+67`
-   Prize: `X=8400, Y=5400`

Solution:

-   80 presses of A and 40 presses of B align the claw with the prize.
-   Total cost: `80*3 + 40*1 = 280 tokens`.

**Part 2:**  
Input (adjusted prize position):

-   Button A: `X+94, Y+34`
-   Button B: `X+22, Y+67`
-   Prize: `X=10000000008400, Y=10000000005400`

Solution:

-   Updated calculations with large integers determine new costs.

---

### Results (Based on Input Data)

-   **Part 1 Result:** `37686` tokens.
-   **Part 2 Result:** `77204516023437` tokens.

---

## Learn More

This challenge is part of [Advent of Code](https://adventofcode.com/). Check out the repository for solution code and input data!
