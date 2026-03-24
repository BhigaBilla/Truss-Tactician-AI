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
        
        
        if truss_type == "warren":
            self.obstacles = self._generate_warren_truss()
        else:
            self.obstacles = self._generate_pratt_truss()
            
       
        self.defects = self._generate_random_defects(num_defects)

    def _generate_pratt_truss(self):
        obs = []
       
        for i in range(self.size):
            obs.append((0, i))
            obs.append((self.size-1, i))
            
       
        for j in range(0, self.size, 5):
            for i in range(self.size):
                # Leave a gap in the middle (e.g., rows 7, 8, 9) for passage
                if i not in [7, 8, 9]: 
                    obs.append((i, j))
        return set(obs)

    def _generate_warren_truss(self):
        obs = []
        # Diagonal zig-zag pattern
        for i in range(self.size):
            obs.append((0, i)) # Bottom Chord
            obs.append((self.size-1, i)) # Top Chord
           
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
                
                defects[(x, y)] = random.randint(1, 10) * 10 
                count += 1
        return defects

    def is_valid(self, pos):
        """Checks if a position is within bounds and not an obstacle."""
        x, y = pos
        return 0 <= x < self.size and 0 <= y < self.size and pos not in self.obstacles
