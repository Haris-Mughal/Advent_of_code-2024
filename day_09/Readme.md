# 🎄 Advent of Code - Day 9: Disk Fragmenter 💾

![Advent of Code Animation](https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif)

## Challenge Description

Help an amphipod compact its hard drive for more contiguous free space. The disk map is represented in a **dense format** that alternates between file lengths and free space lengths.

Your tasks are:

### Part 1: File Compaction (One Block at a Time)

-   Move file blocks **one at a time** to fill the leftmost free spaces.
-   Calculate the **filesystem checksum** based on the final compacted arrangement.

### Part 2: File Compaction (Whole Files)

-   Move **whole files** to the leftmost free space large enough to fit them.
-   Each file moves once in decreasing order of file ID.
-   Calculate the **filesystem checksum** using the updated arrangement.

---

### Examples

**Input:**  
`2333133121414131402`

**Initial Disk Map Representation:**  
`00...111...2...333.44.5555.6666.777.888899`

#### Part 1 (One Block at a Time):

Compact the files step by step:

-   `0099811188827773336446555566`  
    **Checksum:** `1928`

#### Part 2 (Whole Files):

Compact the files step by step:

-   `00992111777.44.333....5555.6666.....8888..`  
    **Checksum:** `2858`

---

## Results (Using My Input)

-   **Part 1 Filesystem Checksum:** `6435922584968`
-   **Part 2 Filesystem Checksum:** `6469636832766`

---

## How It Works

1. **Disk Map:** Interpret alternating numbers as file and free space lengths.
2. **Compaction:** Rearrange blocks or files based on the part's rules.
3. **Checksum Calculation:** Sum of `(position × file ID)` for all blocks containing file IDs.

---

## Learn More

This challenge is part of [Advent of Code](https://adventofcode.com/). Check out the repository for code and input data!
