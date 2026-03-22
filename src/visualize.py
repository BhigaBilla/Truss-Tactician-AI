import matplotlib.pyplot as plt

def animate_inspection(env, path):
    grid = np.zeros((env.size, env.size))
    for x, y in env.obstacles: grid[x, y] = 1
    for x, y in env.defects: grid[x, y] = 0.5
    
    plt.imshow(grid.T, cmap='Greys', origin='lower')
    px, py = zip(*path)
    plt.plot(px, py, marker='o', color='red', label='Drone Path')
    plt.title("AeroScan-AI: Structural Inspection Path")
    plt.legend()
    plt.show()
