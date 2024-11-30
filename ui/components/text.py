# ui/components/text.py

from PIL import ImageDraw
from .base import Component

class Text(Component):
    def __init__(self, x, y, text, font, style=None):
        self.x = x
        self.y = y
        self.text = text
        self.font = font
        self.style = style or {}

    def render(self, draw: ImageDraw):
        fill = self.style.get("color", 0)  # Default color: black
        draw.text((self.x, self.y), self.text, font=self.font, fill=fill)
