# 🎄 Advent of Code - Day 8: Resonant Collinearity 🌌

![Advent of Code Animation](https://media.giphy.com/media/xT9IgG50Fb7Mi0prBC/giphy.gif)

## Problem Overview

This repository contains my solutions for **Day 8: Resonant Collinearity** from the Advent of Code 2024 challenge. The puzzle focuses on analyzing antenna signals and their impact on specific grid positions, known as antinodes, based on resonance rules. The challenge is split into two parts, each adding complexity to the conditions under which antinodes are created.

---

## Problem Statement

### Part 1

Given a grid map with antennas emitting specific frequencies, identify all **unique locations** within the grid that contain antinodes. An antinode is created when:

-   Two antennas of the same frequency are in a straight line.
-   One antenna is exactly **twice as far** from a point as the other.

### Part 2

In addition to the above conditions, an antinode can now occur at **any grid position in line with at least two antennas** of the same frequency, regardless of distance. This includes the positions of antennas themselves (unless the antenna is the only one with its frequency).

---

## Input Format

-   The input is a 2D grid with:
    -   `.` representing empty spaces.
    -   Lowercase letters, uppercase letters, or digits representing antenna frequencies.

---

## Output

-   **Part 1**: Total number of unique grid positions containing an antinode.
-   **Part 2**: Updated total number of unique antinode positions with relaxed rules.

---

## Solutions

### Part 1: Counting Antinodes Based on Distance Rules

The solution involves:

1. Parsing the grid to locate antennas and their frequencies.
2. Identifying pairs of antennas with the same frequency.
3. Calculating potential antinode positions between each pair, ensuring the distance condition is satisfied.
4. Tracking unique antinode positions within the bounds of the map.

### Part 2: Extended Resonant Harmonics

The updated solution:

1. Adds all grid positions in line with at least two antennas of the same frequency as antinodes.
2. Includes positions of antennas as antinodes if there are at least two antennas of the same frequency.

---

## Results

-   **Part 1 Output**: `301` unique antinode locations.
-   **Part 2 Output**: `1019` unique antinode locations.

---

### How to use

1. Clone the repository:
    ```bash
    git clone <repository_url>
    ```
