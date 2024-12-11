# 🎄 Advent of Code - Day 11: Plutonian Pebbles 🪨✨

![Advent of Code Animation](https://media.giphy.com/media/l41lI4bYmcsPJX9Go/giphy.gif)

## Challenge Description

Explore the enigmatic physics-defying stones of Pluto! Each stone evolves following specific rules every time you blink.

Your tasks are:

### Part 1: Blinking Stones

-   Simulate the stones' transformations for **25 blinks**.
-   Determine the **total number of stones** after the blinks.

### Part 2: Extended Evolution

-   Simulate the stones' transformations for **75 blinks**.
-   Determine the **total number of stones** after these extended transformations.

---

### Examples

**Initial Arrangement:**  
`125 17`

#### Blinking Steps:

**After 1 Blink:**  
`253000 1 7`

**After 2 Blinks:**  
`253 0 2024 14168`

**After 3 Blinks:**  
`512072 1 20 24 28676032`

**After 4 Blinks:**  
`512 72 2024 2 0 2 4 2867 6032`

---

## Results (Using My Input)

-   **Part 1 Result (25 Blinks):** `172484` stones.
-   **Part 2 Result (75 Blinks):** `205913561055242` stones.

---

## How It Works

1. **Transformation Rules:**

    - If a stone is `0`: Replace it with `1`.
    - If a stone's number has an **even number of digits**: Split it into two stones.
    - Otherwise: Multiply the stone's number by `2024`.

2. **Simulation Process:** Apply the rules to all stones simultaneously for the required number of blinks.

3. **Output Calculation:** Count the total stones after the transformations.

---

## Learn More

This challenge is part of [Advent of Code](https://adventofcode.com/). Check out the repository for the code and input data!
