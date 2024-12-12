# 🎄 Advent of Code - Day 12: Garden Groups 🌱

![Advent of Code Animation](https://media.giphy.com/media/xUPGcdhiQO2cr2EbTG/giphy.gif)

## Challenge Description

You're helping Elves calculate the fencing required for a complex arrangement of garden plots. Each garden plot grows a specific plant, represented by a **single letter**, and touching plots of the same plant form a **region**. You need to calculate the **total price of fencing** for all regions on the map.

### Part 1: Fencing Cost Based on Perimeter

-   **Area:** Count of plots in a region.
-   **Perimeter:** Number of sides not touching another plot of the same type.
-   **Price per Region:** Multiply **area** by **perimeter**.
-   **Total Price:** Sum of all region prices.

### Part 2: Fencing Cost Based on Sides

-   **Sides:** Each straight section of fence counts as one side.
-   **Price per Region:** Multiply **area** by **number of sides**.
-   **Total Price:** Sum of all region prices.

---

### Examples

#### Input Map (4x4 Example):

AAAA <br />
BBCD <br />
BBCC <br />
EEEC

#### Part 1:

-   **Regions:**
    -   A (area=4, perimeter=10, price=40)
    -   B (area=4, perimeter=8, price=32)
    -   C (area=4, perimeter=10, price=40)
    -   D (area=1, perimeter=4, price=4)
    -   E (area=3, perimeter=8, price=24)
-   **Total Price:** `40 + 32 + 40 + 4 + 24 = 140`

#### Part 2:

-   **Regions:**
    -   A (area=4, sides=4, price=16)
    -   B (area=4, sides=4, price=16)
    -   C (area=4, sides=8, price=32)
    -   D (area=1, sides=4, price=4)
    -   E (area=3, sides=4, price=12)
-   **Total Price:** `16 + 16 + 32 + 4 + 12 = 80`

---

### Results (Using My Input)

-   **Part 1 Total Fencing Cost (Based on Perimeter):** `1,471,452`
-   **Part 2 Total Fencing Cost (Based on Sides):** `863,366`

---

## How It Works

1. **Input Map:** Represents garden plots with single letters.
2. **Region Detection:** Group connected plots of the same type into regions.
3. **Price Calculation:** Use the area and either perimeter or sides to calculate the price per region.

---

## Learn More

This challenge is part of [Advent of Code](https://adventofcode.com/). Check out the repository for code and input data!
