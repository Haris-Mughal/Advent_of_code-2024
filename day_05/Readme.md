# 🎄 Advent of Code - Day 5: Print Queue 🖨️

![Advent of Code Animation](https://user-images.githubusercontent.com/your-gif-link.gif)

## Challenge Description

Manage a **print queue** for sleigh safety manual updates by:

1. Identifying updates already in the correct order (Part 1).
2. Reordering the incorrect updates using page ordering rules (Part 2).

Each update has a **middle page number**, and the goal is to calculate the sum of these middle numbers for:

-   Correctly ordered updates.
-   Reordered invalid updates.

---

### Example

**Part 1:**  
For a correctly ordered update `75,47,61,53,29`:

-   Verify the order satisfies rules like `75|47` and `61|53`.
-   Calculate the middle page (`61`).

**Part 2:**  
For an incorrectly ordered update `97,13,75,29,47`:

-   Reorder to `97,75,47,29,13` using rules.
-   Calculate the middle page (`47`).

---

## Results (According to my data)

-   **Part 1 Sum of Middle Pages (Correct Updates):** `6949`
-   **Part 2 Sum of Middle Pages (Reordered Updates):** `4145`

---

## Learn More

This challenge is part of [Advent of Code](https://adventofcode.com/). Check the repository for code and input data!
