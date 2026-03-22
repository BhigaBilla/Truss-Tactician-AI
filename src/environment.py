import numpy as np
import random

class StructuralGrid:
    def __init__(self, size=20, num_defects=5, truss_type="pratt", seed=42):
        """
        size: Grid dimensions (N x N)
        num_defects: Number of damage points to generate
        truss_type: "pratt" or "warren" for different obstacle designs
        seed: Fixed seed for reproducibility [cite: 21]
        """
        self.size = size
        self.seed = seed
        random.seed(seed)
        np.random.seed(seed)
        
        # Define Mechanical Obstacles (Truss Members) [cite: 66-70]
        if truss_type == "warren":
            self.obstacles = self._generate_warren_truss()
        else:
            self.obstacles = self._generate_pratt_truss()
            
        # Dynamically generate defects (Damage Points)
        self.defects = self._generate_random_defects(num_defects)

    def _generate_pratt_truss(self):
        obs = []
        # Top and Bottom Chords (Mechanical boundaries)
        for i in range(self.size):
            obs.append((0, i))
            obs.append((self.size-1, i))
        # Vertical struts every 5 units
        for j in range(0, self.size, 5):
            for i in range(self.size):
                obs.append((i, j))
        return set(obs)

    def _generate_warren_truss(self):
        obs = []
        # Diagonal zig-zag pattern
        for i in range(self.size):
            obs.append((0, i)) # Bottom Chord
            obs.append((self.size-1, i)) # Top Chord
            
            # Diagonal member logic: y = x and y = (size-1) - x
            # We only place them if they aren't blocking the entire grid
            if i % 2 == 0: 
                obs.append((i, i))
                obs.append((self.size-1-i, i))
        return set(obs)

    def _generate_random_defects(self, num):
        defects = {}
        count = 0
        while count < num:
            x = random.randint(1, self.size - 2)
            y = random.randint(1, self.size - 2)
            # Ensure defect is not on a truss beam and not at drone start positions
            if (x, y) not in self.obstacles and (x, y) != (1,1):
                # FIXED: Random weight between 10 and 100 for 'Severity'
                defects[(x, y)] = random.randint(1, 10) * 10 
                count += 1
        return defects

    def is_valid(self, pos):
        """Checks if a position is within bounds and not an obstacle."""
        x, y = pos
        return 0 <= x < self.size and 0 <= y < self.size and pos not in self.obstacles
