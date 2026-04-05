# Truss-Tactician-AI: Adversarial Drone-Based Structural Inspection

## Project Overview
This project automates the task of structural health monitoring using autonomous robotics and classical AI. It simulates a competitive environment where two drones navigate a mechanical truss grid modeled after Pratt and Warren truss geometries. The goal is to identify and scan critical failure points like cracks and corrosion while managing battery and safety constraints.

## Methodology and AI Techniques
The system integrates three primary AI components to bridge the gap between structural analysis and autonomous navigation.

### State-Space Search (A*)
A* search is used for battery-efficient pathfinding between structural members.
* State Representation: The environment is a discrete 2D grid where truss members act as obstacles.
* Heuristic: Manhattan distance is utilized to ensure the shortest orthogonal path in a grid environment.
* Cost Function: The search expands nodes based on the standard f(n) = g(n) + h(n) formula, where g(n) represents the actual path cost from the start.

### Adversarial Search (Minimax with Alpha-Beta Pruning)
This technique handles strategic target selection when drones compete for high-value inspection points.
* Global Evaluation: The maximizing drone simulates future moves to select a target that maximizes its score while considering the opponent's proximity.
* Decision Quality: This approach avoids premature convergence to suboptimal local solutions.
* Optimization: Alpha-beta pruning reduces the number of expanded nodes in the search tree, ensuring real-time performance even as the grid size increases.

### Constraint Satisfaction (CSP)
CSP is used for real-time safety and collision avoidance.
* Forward Checking: Before executing a move, the drone validates that the next state does not violate safety radius constraints relative to the other drone or structural truss members.

## Project Structure
The repository is organized into a modular package structure to ensure clarity:

* /src: The core engine.
    * environment.py: Defines mechanical truss geometries and crack generation.
    * search.py: Implements the A* pathfinding algorithm.
    * adversarial.py: Contains the minimax evaluation logic and target selection.
    * visualize.py: Handles the rendering of inspection paths using matplotlib.
* /results: Stores performance data for analysis.
    * /logs: CSV records of nodes expanded and execution time.
    * /plots: Saved figures of drone paths for report inclusion.
* /docs: Repository for the project proposal and final report.

## How to Run and Reproduce Results

### Installation
1. Clone the repository:
   git clone https://github.com/BhigaBilla/Truss-Tactician-AI.git

2. Install dependencies:
   pip install -r requirements.txt

### Running Test Cases
To match professional AI report standards, you can run three distinct scenarios by adjusting parameters in main.py:

| Test Case | Configuration | Evaluation Goal |
| :--- | :--- | :--- |
| Simple | size=10, defects=3 | Baseline A* efficiency check. |
| Medium | size=20, defects=6 | Path optimization in medium-density grids. |
| Dense | size=30, defects=10 | Stress-testing Alpha-Beta Pruning speed. |

Run the simulation with:
python main.py
