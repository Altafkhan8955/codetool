from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

def generate_og_image(title, description):
    width, height = 1200, 630
    # Create image
    image = Image.new('RGB', (width, height), color=(15, 23, 42))
    draw = ImageDraw.Draw(image)
    # Load fonts
    try:
        title_font = ImageFont.truetype("arial.ttf", 60)
        desc_font = ImageFont.truetype("arial.ttf", 30)
    except:
        title_font = ImageFont.load_default()
        desc_font = ImageFont.load_default()
    # Draw title
    draw.text((60, 200), title, font=title_font, fill=(255, 255, 255))
    # Draw description
    draw.text((60, 350), description, font=desc_font, fill=(180, 180, 180))
    # Save to memory
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer