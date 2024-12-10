# 🎄 Advent of Code - Day 10: Hoof It 🦌

![Advent of Code Animation](https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif)

## Challenge Description

You're tasked with helping a reindeer navigate a topographic map to find hiking trails. The map contains various trailheads, and your job is to calculate the number of reachable trailheads and their ratings.

### Part 1: Trailhead Scores

-   A trailhead is any position with a height of **0**.
-   Your task is to calculate the score of each trailhead, which is the number of **9-height** positions reachable from that trailhead via a hiking trail.
-   The hiking trail must always increase by exactly 1 in height at each step, and trails can only move up, down, left, or right.

#### Example:

Given the following map:

0123 <br/>
1234 <br/>
8765 <br/>
9876

-   The trailhead at the top-left corner has a score of 1 because it can reach a 9 at the bottom-left.
-   The sum of the scores of all trailheads is the final result for Part 1.

### Part 2: Trailhead Ratings

-   In this part, the task is to calculate the **rating** of each trailhead, which is the number of **distinct hiking trails** that begin at that trailhead.
-   Hiking trails can take different paths to reach the 9-height positions, and each unique path counts towards the rating.

#### Example:

For a map with the following layout:

.....0. <br/>
..4321. <br/>
..5..2. <br/>
..6543. <br/>
..7..4. <br/>
..8765. <br/>
..9....

-   The trailhead at the top-left has a rating of 3, as there are exactly three distinct hiking trails that start at this position.

### Examples

**Input:**  
`89010123 78121874 87430965 96549874 45678903 32019012 01329801 10456732`

#### Part 1 (Trailhead Scores):

-   The trailheads have scores of `5, 6, 5, 3, 1, 3, 5, 3, 5`.
-   The sum of all trailhead scores: **36**.

#### Part 2 (Trailhead Ratings):

-   The ratings for the trailheads are `20, 24, 10, 4, 1, 4, 5, 8, 5`.
-   The sum of all trailhead ratings: **81**.

---

## Results (Using My Input)

-   **Part 1 Trailhead Scores Sum:** `789`
-   **Part 2 Trailhead Ratings Sum:** `1735`

---

## How It Works

1. **Trailhead Identification:** Identify positions with a height of 0, which are the starting points of hiking trails.
2. **Trail Exploration:** Explore all possible hiking trails from each trailhead, ensuring that each trail always increases by exactly 1 in height and doesn't move diagonally.
3. **Score Calculation (Part 1):** Count the number of reachable 9-height positions for each trailhead.
4. **Rating Calculation (Part 2):** Count the number of distinct hiking trails that start at each trailhead.

---

## Learn More

This challenge is part of [Advent of Code](https://adventofcode.com/). Check out the repository for code and input data!
