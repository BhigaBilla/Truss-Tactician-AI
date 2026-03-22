# Truss-Tactician-AI: Adversarial Drone-Based Structural Inspection

## 1. Project Overview
This project applies **Classical AI techniques** (Search, Adversarial Logic, and CSPs) to automate the inspection of mechanical truss structures. [cite_start]Two competing drones must prioritize scanning high-value "Damage Points" (cracks/corrosion) while navigating complex steel trusses and avoiding collisions. [cite: 4, 11]

## 2. AI Techniques Used
* [cite_start]**State-Space Search ($A^*$):** Battery-efficient pathfinding using Manhattan Distance. [cite: 42, 43]
* **Adversarial Search (Minimax + Alpha-Beta):** Strategic target selection against a competing agent. [cite: 12]
* [cite_start]**CSP (AC-3/Forward Checking):** Real-time collision avoidance and safety zone maintenance. [cite: 12]

## 3. Mechanical Domain Merit
The simulation environment uses grid-based modeling of **Pratt and Warren Truss** geometries. [cite_start]This bridges the gap between Mechanical Structural Analysis and Autonomous Robotics. [cite: 10, 47]

## 4. How to Run
```bash
pip install -r requirements.txt
python main.py
