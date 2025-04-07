import os
from gui_helpers import showError

def load_board(file_path):
    try:
        if not os.path.exists(file_path):
            showError(f"{FileNotFoundError}: Board file {file_path} does not exist.")
        if not os.path.isfile(file_path):
            showError(f"Error: {file_path} is not a valid file.")

        board = []
        line_length = None
        with open(file_path, 'r') as file:
            for line in file:
                if line_length is None:
                    line_length = len(line.strip())
                elif len(line.strip()) != line_length:
                    print(f"Error: Inconsistent line lengths in board file.")
                    return None

                board_line = [1 if char == 'X' else 0 for char in line.strip()]
                if not all(char in ['X', '.'] for char in line.strip()):
                    print(f"Error: Invalid character in board file.")
                    return None
                board.append(board_line)
        return board
    
    except Exception as e:
        showError(f"Error loading board: {e}")
        return None

def save_board_to_file(game, file_path):
    with open(file_path, 'w') as file:
        for row in game.board:
            line = ''.join(['X' if cell == 1 else '.' for cell in row])
            file.write(line + '\n')
