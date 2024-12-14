# Advent of Code - Day 14: Restroom Redoubt 🛠️

![Robot Simulation](https://media.giphy.com/media/26FPnwz3wDUli7GU0/giphy.gif)

## Challenge Description

The Easter Bunny Headquarters bathroom is protected by a swarm of security robots. To navigate safely, you must predict their movements based on their initial positions and velocities. Robots teleport at edges, and their movement forms predictable patterns over time.

---

### Rules

1. **Part 1:**  
   Calculate the safety factor after simulating the robots' movements for 100 seconds. The safety factor is the product of the number of robots in each of the four quadrants.  
   Robots on the midlines are not counted in any quadrant.

2. **Part 2:**  
   Determine the minimum number of seconds needed for the robots to align into an Easter egg shape resembling a Christmas tree.

---

### Example

**Part 1:**  
Input:

-   Initial robot positions and velocities.  
    Example positions:  
    `p=0,4 v=3,-3`  
    `p=6,3 v=-1,-3`

**Output After 100 Seconds:**

-   Quadrants contain 1, 3, 4, and 1 robot, respectively.
-   Safety factor: `1 * 3 * 4 * 1 = 12`.

**Part 2:**

-   Fewest seconds for Christmas tree alignment: `7603`.

---

### Results (Based on Input Data)

-   **Part 1 Result:** `224438715`.
-   **Part 2 Result:** `7603`.

---

## Learn More

This challenge is part of [Advent of Code](https://adventofcode.com/). Check out the repository for solution code and input data!
