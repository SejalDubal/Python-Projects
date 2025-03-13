# Page Replacement Algorithm Simulator

This project simulates various **Page Replacement Algorithms** used in operating systems to manage memory efficiently. It provides a graphical user interface (GUI) for visualizing how different algorithms handle page faults and replace pages in memory.

## Features
- **Supported Algorithms**:
  - FIFO (First In First Out)
  - LIFO (Last In First Out)
  - LRU (Least Recently Used)
  - MRU (Most Recently Used)
  - Optimal Page Replacement
  - Random Page Replacement
- **Visualization**: Real-time visualization of page frames, page faults, and hit/miss ratios.
- **Graphical Comparison**: Compare the performance of all algorithms using a bar chart.
- **Theory Section**: Learn about the working and theory behind each algorithm.

## Screenshots
![Screenshot 2025-03-13 194108](https://github.com/user-attachments/assets/de6f6649-29ab-4b39-97ff-79128cf5c798)
*Main Menu of the Simulator*

![Screenshot 2025-03-13 194126](https://github.com/user-attachments/assets/ccccec73-6e81-4bfa-be22-6e3e485e903c)
*Visualization of FIFO Algorithm*

![Screenshot 2025-03-13 194140](https://github.com/user-attachments/assets/98e8ff88-1c16-4cce-8b5c-3f715549905d)
*Comparison Graph of All Algorithms*

![Screenshot 2025-03-13 194210](https://github.com/user-attachments/assets/de868c3c-83c7-4e06-97ef-ea8855b787e9)
*Theory Page*

## Prerequisites
- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- Matplotlib (`pip install matplotlib`)

## How to Run
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/page-replacement-simulator.git
   cd page-replacement-simulator
## Using the Simulator

- Select an algorithm from the dropdown menu.

- Enter the number of frames.

- Enter the page reference string (e.g., 1 2 3 4 1 2 5 1 2 3 4 5).

- Click Visualise to see the algorithm in action.

- Click Compare All Algorithms to generate a comparison graph.

- Click Theory to learn about the algorithms.

# Algorithms Overview

## 1. FIFO (First In First Out)
Description: The oldest page in memory is replaced when a new page needs to be loaded.

Advantages:

Simple to implement.

Disadvantages:

Suffers from Belady's Anomaly, where increasing the number of frames can lead to more page faults.

Use Case: Basic memory management systems.

## 2. LIFO (Last In First Out)
Description: The most recently added page is replaced.

Advantages:

Easy to implement.

Disadvantages:

Poor performance in most scenarios.

Use Case: Rarely used in practice.

## 3. LRU (Least Recently Used)
Description: The page that has not been used for the longest time is replaced.

Advantages:

More efficient than FIFO.

Works well in most real-world scenarios.

Disadvantages:

Requires additional overhead to track page usage.

Use Case: Systems where recent usage patterns are important.

## 4. MRU (Most Recently Used)
Description: The most recently used page is replaced.

Advantages:

Useful in specific scenarios where recently used pages are less likely to be used again.

Disadvantages:

Not as commonly used as LRU.

Use Case: Specialized memory management systems.

## 5. Optimal Page Replacement
Description: The page that will not be used for the longest time in the future is replaced.

Advantages:

Provides the lowest possible page fault rate.

Disadvantages:

Requires future knowledge of page references, making it impractical for real-world systems.

Use Case: Theoretical benchmarking of other algorithms.

## 6. Random Page Replacement
Description: A random page is selected for replacement.

Advantages:

Simple to implement.

Disadvantages:

Unpredictable performance.

Use Case: Systems where simplicity is more important than performance.
