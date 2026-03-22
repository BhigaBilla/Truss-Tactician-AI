import time
import os
from src.environment import StructuralGrid
from src.search import a_star
from src.adversarial import evaluation_function
from src.visualize import animate_inspection

def run_simulation():
    # 1. Setup Mechanical Environment
    env = StructuralGrid(size=20)
    drone_a_pos = (1, 1)
    drone_b_pos = (18, 18)
    total_score_a = 0
    
    print("--- AeroScan-AI: Structural Inspection Initialized ---")
    print(f"Truss Grid Size: {env.size}x{env.size}")
    print(f"Detected Damage Points: {len(env.defects)}")
    print("-" * 50)

    # 2. Strategy Phase (Adversarial Target Selection)
    # We use Minimax logic to pick the best target based on priority and competition
    target_a = evaluation_function(drone_a_pos, drone_b_pos, env.defects)
    
    if target_a:
        print(f"[STRATEGY] Drone A targeting high-priority crack at: {target_a}")
        print(f"[STRATEGY] Mechanical Priority Weight: {env.defects[target_a]}")
    else:
        print("No targets available.")
        return

    # 3. Execution Phase (A* Pathfinding)
    # This generates the performance metrics for your Final Report [cite: 70]
    start_time = time.perf_counter()
    path_a, nodes = a_star(env, drone_a_pos, target_a)
    end_time = time.perf_counter()

    # 4. Results Compilation
    exec_time_ms = (end_time - start_time) * 1000
    print("-" * 50)
    print(f"--- PERFORMANCE ANALYSIS ---")
    print(f"Algorithm: A* Search with Manhattan Heuristic")
    print(f"Computation Time: {exec_time_ms:.4f} ms")
    print(f"State-Space Nodes Expanded: {nodes}")
    print(f"Path Length: {len(path_a)} units")
    print("-" * 50)

    # 5. Presentation Layer (Visualization) 
    # This satisfies the requirement for "high-quality visualization"
    print("Generating Graphical Representation...")
    animate_inspection(env, path_a)

if __name__ == "__main__":
    # Ensure results directory exists for logs
    if not os.path.exists('results/logs'):
        os.makedirs('results/logs')
    
    run_simulation()
