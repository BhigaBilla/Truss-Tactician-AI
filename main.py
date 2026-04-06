import time
import os
from src.environment import StructuralGrid
from src.search import a_star

from src.adversarial import minimax_alpha_beta, evaluation_function 
from src.visualize import animate_inspection, reconstruct_path

def run_simulation(size=30, num_defects=10, truss_type="pratt", seed=99):
   
    env = StructuralGrid(size=size, num_defects=num_defects, 
                         truss_type=truss_type, seed=seed)
    
    drone_a_pos = (1, 1)
    drone_b_pos = (size-2, size-2)
    
    print(f"\n--- Starting AeroScan-AI Dual-Drone Simulation: {size}x{size} ({truss_type.upper()}) ---")
    
    
    score_a, target_a = minimax_alpha_beta(
        drone_a_pos, drone_b_pos, env.defects, 
        depth=2, alpha=-float('inf'), beta=float('inf'), is_maximizing=True
    )
    
    
    remaining_defects = {k: v for k, v in env.defects.items() if k != target_a}
 
    scores_b = evaluation_function(drone_b_pos, drone_a_pos, remaining_defects)
    target_b = max(scores_b, key=scores_b.get) if scores_b else None
    
    if not target_a or not target_b:
        print("Error: Could not identify valid targets for both drones.")
        return


    start_a = time.perf_counter()
    came_from_a, nodes_a = a_star(env, drone_a_pos, target_a)
    exec_a = (time.perf_counter() - start_a) * 1000
    
    start_b = time.perf_counter()
    came_from_b, nodes_b = a_star(env, drone_b_pos, target_b)
    exec_b = (time.perf_counter() - start_b) * 1000

    
    print("-" * 60)
    print(f"Drone A (Minimax) -> Target: {target_a} | Nodes: {nodes_a} | Time: {exec_a:.2f} ms")
    print(f"Drone B (Greedy)  -> Target: {target_b} | Nodes: {nodes_b} | Time: {exec_b:.2f} ms")
    print("-" * 60)

    path_a = reconstruct_path(came_from_a, drone_a_pos, target_a)
    path_b = reconstruct_path(came_from_b, drone_b_pos, target_b)
    animate_inspection(env, path_a, path_b, target_a, target_b, size)

if __name__ == "__main__":
    # Define the Test Cases for the Final Report Table
    test_cases = [
        {"name": "Case 1: Simple", "size": 10, "defects": 3, "type": "pratt", "seed": 1},
        {"name": "Case 2: Medium", "size": 20, "defects": 6, "type": "pratt", "seed": 42},
        {"name": "Case 3: Dense", "size": 30, "defects": 10, "type": "warren", "seed": 99}
    ]

    print("=" * 60)
    print("AeroScan-AI: Batch Performance Testing Initialized")
    print("=" * 60)

    for case in test_cases:
        print(f"\n[RUNNING] {case['name']}")
        
        run_simulation(
            size=case['size'], 
            num_defects=case['defects'], 
            truss_type=case['type'], 
            seed=case['seed']
        )
        
        print(f"[COMPLETED] {case['name']}")
        print("-" * 60)
        
    print("\nBatch processing complete.")