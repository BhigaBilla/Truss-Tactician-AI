import matplotlib.pyplot as plt
import numpy as np




def animate_inspection(env, path_a, path_b, target_a, target_b):
    fig, ax = plt.subplots(figsize=(10, 8))
    grid_display = np.zeros((env.size, env.size))
    for x, y in env.obstacles: grid_display[x, y] = 1
    
    ax.imshow(grid_display, cmap='Greys', origin='upper', alpha=0.2)
    
    # Plot Defects
    for (x, y), weight in env.defects.items():
        ax.scatter(y, x, s=weight*3, c='red', marker='x', zorder=3)
        ax.text(y+0.3, x+0.3, f"W:{weight}", fontsize=9, color='darkred')

    # Plot Drone A (Blue)
    if path_a:
        px, py = zip(*path_a)
        ax.plot(py, px, color='blue', linewidth=2, label='Drone A Path')
        ax.scatter(py[0], px[0], color='blue', s=100, marker='o', label='A Start')
        ax.scatter(target_a[1], target_a[0], color='blue', s=200, marker='*', label='A Target')

    # Plot Drone B (Orange)
    if path_b:
        px, py = zip(*path_b)
        ax.plot(py, px, color='orange', linewidth=2, linestyle='--', label='Drone B Path')
        ax.scatter(py[0], px[0], color='orange', s=100, marker='o', label='B Start')
        ax.scatter(target_b[1], target_b[0], color='orange', s=200, marker='*', label='B Target')

    plt.title("Truss-Tactician: Dual-Drone Adversarial Inspection")
    plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1))
    plt.grid(alpha=0.3)
    plt.show()