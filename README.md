# Truss-Tactician-AI: Adversarial Drone-Based Structural Inspection

## 1. Project Overview
This project automates the high-risk task of **Structural Health Monitoring (SHM)** using autonomous robotics and Classical AI techniques. [cite_start]It simulates a competitive environment where two drones navigate a mechanical truss grid—modeled after **Pratt and Warren Truss** geometries—to identify and scan critical failure points (cracks and corrosion) while managing battery and safety constraints[cite: 10, 47].

## 2. Methodology & AI Techniques
The system integrates three core AI pillars to bridge the gap between structural analysis and autonomous navigation:

### **A. State-Space Search ($A^*$)**
Used for battery-efficient pathfinding between structural members.
* **State Representation**: A discrete 2D grid $(x, y)$ where truss members act as obstacles [cite: 58-59].
* [cite_start]**Heuristic ($h(n)$)**: **Manhattan Distance** ($|x_1 - x_2| + |y_1 - y_2|$) is utilized to ensure the shortest orthogonal path in a grid environment [cite: 62-63].
* [cite_start]**Cost Function**: The search expands nodes based on $f(n) = g(n) + h(n)$, where $g(n)$ is the actual path cost from the start [cite: 60-61].

### **B. Adversarial Search (Minimax with Alpha-Beta Pruning)**
Used for strategic target selection when competing against another drone for high-value inspection points.
* **Global Evaluation**: Unlike a simple greedy approach, the "Maximizing" drone simulates future moves to select a target that maximizes its score while considering the opponent's proximity [cite: 93-98].
* [cite_start]**Decision Quality**: This "best-choice" move systematicially avoids premature convergence to suboptimal local solutions [cite: 103-104].
* [cite_start]**Optimization**: **Alpha-Beta Pruning** is implemented to reduce the number of expanded nodes in the search tree, ensuring real-time performance even as the grid size increases .

### **C. Constraint Satisfaction (CSP)**
Used for real-time safety and collision avoidance.
* **Forward Checking**: Before executing a move, the drone validates that the next state does not violate "Safe Distance" constraints relative to the other drone or structural truss members.

---

## 3. Project Structure
The repository is organized into a modular package structure to ensure codebase clarity and professional documentation:

* **`/src`**: The core engine.
    * `environment.py`: Defines the mechanical truss geometries and dynamic crack generation.
    * [cite_start]`search.py`: Implements the $A^*$ pathfinding algorithm [cite: 72-80].
    * [cite_start]`adversarial.py`: Contains the Minimax evaluation logic and target selection [cite: 92-101].
    * `visualize.py`: Handles the high-quality `matplotlib` rendering of inspection paths.
* [cite_start]**`/results`**: Stores performance data for academic analysis [cite: 22, 510-511].
    * `/logs`: CSV records of **Nodes Expanded** and **Execution Time**.
    * `/plots`: Saved figures of drone paths for report inclusion.
* **`/docs`**: Repository for the **Phase 1 Proposal** and **Final Report**.

---

## 4. How to Run & Reproduce Results

### **Installation**
1. Clone the repository:  
   `git clone https://github.com/your-username/Truss-Tactician-AI.git`
2. Install dependencies:  
   `pip install -r requirements.txt`

### **Running Test Cases**
[cite_start]To match the comparative analysis standards of professional AI reports, you can run three distinct scenarios by adjusting parameters in `main.py` [cite: 135-136, 178]:

| Test Case | Configuration | Evaluation Goal |
| :--- | :--- | :--- |
| **Simple** | `size=10, defects=3` | Baseline $A^*$ efficiency check. |
| **Medium** | `size=20, defects=6` | Path optimization in medium-density grids. |
| **Dense** | `size=30, defects=10` | Stress-testing Alpha-Beta Pruning speed[cite: 521]. |

```bash
python main.py