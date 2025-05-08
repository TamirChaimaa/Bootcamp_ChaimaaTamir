import time
import os

class GameOfLife:
    def __init__(self, rows, cols, initial_state):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        self.set_initial_state(initial_state)

    def set_initial_state(self, initial_state):
        for x, y in initial_state:
            if 0 <= x < self.rows and 0 <= y < self.cols:
                self.grid[x][y] = 1

    def display(self):
        os.system("cls" if os.name == "nt" else "clear")  # Efface la console
        for row in self.grid:
            print(' '.join(['■' if cell else '·' for cell in row]))
        print()

    def count_live_neighbors(self, x, y):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),         (0, 1),
                      (1, -1),  (1, 0), (1, 1)]
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols:
                count += self.grid[nx][ny]
        return count

    def next_generation(self):
        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for x in range(self.rows):
            for y in range(self.cols):
                neighbors = self.count_live_neighbors(x, y)
                if self.grid[x][y] == 1:
                    if neighbors in [2, 3]:
                        new_grid[x][y] = 1
                else:
                    if neighbors == 3:
                        new_grid[x][y] = 1
        self.grid = new_grid

    def run(self, generations=10, delay=0.5):
        for _ in range(generations):
            self.display()
            self.next_generation()
            time.sleep(delay)

# Exemple d'état initial : un planeur (glider)
initial_state = [
    (1, 2),
    (2, 3),
    (3, 1), (3, 2), (3, 3)
]

game = GameOfLife(rows=20, cols=20, initial_state=initial_state)
game.run(generations=50, delay=0.2)
