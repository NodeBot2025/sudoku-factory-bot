from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def create_interior(puzzles, output_path):
    c = canvas.Canvas(output_path, pagesize=letter)
    for idx, puzzle in enumerate(puzzles):
        c.drawString(100, 750, f"Puzzle {idx+1}")
        y = 700
        for row in puzzle:
            c.drawString(100, y, "  ".join(str(num) for num in row))
            y -= 20
        c.showPage()
    c.save()
