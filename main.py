import time
from src.environment import StructuralGrid
from src.search import a_star
from src.adversarial import evaluation_function
from src.constraints import check_collision_constraint

def run_simulation():
    env = StructuralGrid(size=20)
    drone_a_pos = (1, 1)
    drone_b_pos = (18, 1)
    
    print("--- Starting AeroScan-AI Simulation ---")
    
    # Logic Explanation: Strategy selection [cite: 19]
    target_a = evaluation_function(drone_a_pos, drone_b_pos, env.defects)
    print(f"Drone A strategically targets Crack at {target_a}")

    # Search Execution
    start_time = time.time()
    path_map, nodes = a_star(env, drone_a_pos, target_a)
    end_time = time.time()

    # Data for Results Section [cite: 70]
    print(f"Path found in {(end_time - start_time)*1000:.2f} ms")
    print(f"Nodes expanded: {nodes}")

if __name__ == "__main__":
    run_simulation()
