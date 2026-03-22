import numpy as np

class StructuralGrid:
    def __init__(self, size=20):
        self.size = size
        # 0: Air, 1: Steel Truss (Obstacle), 5: Damage Point
        self.grid = np.zeros((size, size))
        self.obstacles = self._generate_pratt_truss()
        self.defects = {
            (2, 5): 100, (18, 15): 90, (10, 10): 75, 
            (5, 18): 50, (15, 2): 60
        } # (pos): Severity_Weight

    def _generate_pratt_truss(self):
        obs = []
        # Top and Bottom Chords
        for i in range(self.size):
            obs.append((0, i))
            obs.append((self.size-1, i))
        # Vertical and Diagonal Members (Mechanical Simulation)
        for j in range(0, self.size, 5):
            for i in range(self.size):
                obs.append((i, j))
        return set(obs)

    def is_valid(self, pos):
        x, y = pos
        return 0 <= x < self.size and 0 <= y < self.size and pos not in self.obstacles
