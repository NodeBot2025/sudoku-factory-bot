import random

def generate_title(niche):
    adjectives = ["Easy", "Fun", "Brain-Boosting", "Relaxing"]
    return f"{random.choice(adjectives)} Sudoku for {niche}"
