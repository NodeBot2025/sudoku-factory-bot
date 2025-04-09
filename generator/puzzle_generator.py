import random
import numpy as np

def generate_sudoku():
    puzzle = np.zeros((9, 9), dtype=int)
    return puzzle

def format_puzzle(puzzle):
    return "\n".join([" ".join(map(str, row)) for row in puzzle])
