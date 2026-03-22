import matplotlib.pyplot as plt
import numpy as np

def animate_inspection(env, path):
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Create the grid base
    grid_display = np.zeros((env.size, env.size))
    
    # Mark Truss Beams (Obstacles) as dark gray
    for x, y in env.obstacles:
        grid_display[x, y] = 1
        
    # Mark Damage Points (Cracks) as red
    for (x, y), weight in env.defects.items():
        ax.scatter(y, x, s=weight*2, c='red', marker='x', label='Damage Point' if (x,y) == list(env.defects.keys())[0] else "")
        ax.text(y + 0.5, x + 0.5, f"W:{weight}", fontsize=8, color='darkred')

    # Draw the Truss structure using a heat map style
    ax.imshow(grid_display, cmap='Greys', origin='upper', alpha=0.3)
    
    # Draw the A* Path
    if path:
        px, py = zip(*path)
        # We swap x and y for plotting to match grid coordinates
        ax.plot(py, px, color='blue', linewidth=2, label='Drone Path', alpha=0.8)
        # Mark Start and End
        ax.scatter(py[0], px[0], color='green', s=100, label='Drone Start', zorder=5)
        ax.scatter(py[-1], px[-1], color='gold', s=150, marker='*', label='Target Crack', zorder=5)

    # Design elements: Grid lines and Labels
    ax.set_xticks(np.arange(-.5, env.size, 1), minor=True)
    ax.set_yticks(np.arange(-.5, env.size, 1), minor=True)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=0.5, alpha=0.2)
    
    plt.title("Truss-Tactician: Autonomous Structural Inspection")
    plt.xlabel("Truss Span (Width)")
    plt.ylabel("Truss Height")
    plt.legend(loc='upper right', fontsize='small', framealpha=0.9)
    
    print("--- Visualization Window Opened ---")
    plt.show() # This is the command that pops the window up!
