import time
import os
from src.environment import StructuralGrid
from src.search import a_star
from src.adversarial import evaluation_function
from src.visualize import animate_inspection

def run_simulation(size=20, num_defects=5, truss_type="pratt", seed=42):
    """
    size: Grid dimensions (N x N)
    num_defects: Total damage points to generate
    truss_type: "pratt" or "warren" (changes the obstacle design)
    seed: Fixed number for reproducible results
    """
    # 1. Initialize the Environment
    env = StructuralGrid(size=size, num_defects=num_defects, 
                         truss_type=truss_type, seed=seed)
    
    # Start positions for the drones
    drone_a_pos = (1, 1)
    drone_b_pos = (size-2, size-2)
    
    print(f"\n--- Running Simulation: {size}x{size} ({truss_type.upper()}) ---")
    
    # 2. Strategy: Select the best target using Adversarial Logic
    target_a = evaluation_function(drone_a_pos, drone_b_pos, env.defects)
    
    if not target_a:
        print("Error: No valid targets found.")
        return

    # 3. Execution: Run A* Pathfinding
    start_time = time.perf_counter()
    path, nodes = a_star(env, drone_a_pos, target_a)
    end_time = time.perf_counter()

    # 4. Output Performance Metrics (For your Report Table)
    exec_time = (end_time - start_time) * 1000
    print(f"Target Selected: {target_a}")
    print(f"Pathfinding Time: {exec_time:.2f} ms")
    print(f"Nodes Expanded: {nodes}")
    print(f"Path Length: {len(path)} units")

    # 5. Visualization (Satisfies Phase 2 requirements)
    animate_inspection(env, path)

if __name__ == "__main__":
    # CONFIGURATION AREA: Change these values to get different report figures
    # ----------------------------------------------------------------------
    # CASE 1 (Simple): size=10, num_defects=3, truss_type="pratt", seed=1
    # CASE 2 (Medium): size=20, num_defects=6, truss_type="pratt", seed=42
    # CASE 3 (Dense):  size=30, num_defects=10, truss_type="warren", seed=99
    
    run_simulation(
        size=20, 
        num_defects=5, 
        truss_type="pratt", 
        seed=42
    )
