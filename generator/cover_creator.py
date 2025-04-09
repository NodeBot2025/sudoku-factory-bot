from PIL import Image, ImageDraw, ImageFont

def create_cover(title, output_path):
    img = Image.new('RGB', (2550, 3300), color='white')
    d = ImageDraw.Draw(img)
    fnt = ImageFont.load_default()
    d.text((100,100), title, font=fnt, fill=(0,0,0))
    img.save(output_path)
