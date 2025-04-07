import numpy as np
from gui_helpers import showError
from constants import *

class GameOfLife:
    def __init__(self, width, height, randomize=False, file_path=None, survival_rules=[2, 3], birth_rules=[3]):
        if file_path:
            self.board = self.load_board_from_file(file_path)
        elif randomize:
            self.board = np.random.randint(2, size=(height, width))
        else:
            self.board = np.zeros((height, width), dtype=int)

        self.survival_rules = survival_rules
        self.birth_rules = birth_rules

    def load_board_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                if file_path == 'sample_patterns/glider.txt':
                    return np.hstack((np.zeros((51, 15)), np.vstack((np.zeros((20, 100)), np.array([[1 if char == 'X' else 0 for char in line.strip()] for line in lines])))))
                elif file_path == 'sample_patterns/gosper-glider-gun.txt':
                    return np.vstack((np.array([[1 if char == 'X' else 0 for char in line.strip()] for line in lines]), np.zeros((7, 100))))
                elif file_path == 'sample_patterns/pulsar.txt':
                    new_array = np.vstack((np.zeros((3, 100)), np.array([[1 if char == 'X' else 0 for char in line.strip()] for line in lines]), np.zeros((5, 100))))
                    return new_array[:, 16:]
                else:
                    return np.array([[1 if char == 'X' else 0 for char in line.strip()] for line in lines])
        except Exception as e:
            showError(f'Failed to load saved board: {e}')
            return np.random.randint(2, size=(WINDOW_HEIGHT // CELL_SIZE, WINDOW_WIDTH // CELL_SIZE))

    def update_board(self):
        if not self.is_board_valid():
            raise ValueError("Invalid board state")
        new_board = self.board.copy()
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                new_board[i, j] = self.update_cell(i, j)
        self.board = new_board

    def update_cell(self, x, y):
        num_alive_neighbors = sum([self.board[i, j] for i in range(x-1, x+2)
                                   for j in range(y-1, y+2) if (i != x or j != y) and 0 <= i < self.board.shape[0] and 0 <= j < self.board.shape[1]])
        
        if self.board[x, y] == 1:
            return 1 if num_alive_neighbors in self.survival_rules else 0
        else:
            return 1 if num_alive_neighbors in self.birth_rules else 0
    
    def is_board_valid(self):
        if not isinstance(self.board, np.ndarray):
            return False
        if self.board.ndim != 2:
            return False
        if not np.all(np.isin(self.board, [0, 1])):
            return False
        return True
