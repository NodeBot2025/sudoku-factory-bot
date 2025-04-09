import os
from generator.puzzle_generator import generate_sudoku
from generator.interior_creator import create_interior
from generator.cover_creator import create_cover
from metadata.title_generator import generate_title
from uploader.kdp_uploader import upload_to_kdp
from config import *

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

for i in range(BOOK_COUNT):
    title = generate_title("Seniors")
    puzzles = [generate_sudoku() for _ in range(PUZZLES_PER_BOOK)]

    interior_path = f"{OUTPUT_DIR}/{title}_interior.pdf"
    create_interior(puzzles, interior_path)

    cover_path = f"{OUTPUT_DIR}/{title}_cover.png"
    create_cover(title, cover_path)

    upload_to_kdp(title, interior_path, cover_path)
