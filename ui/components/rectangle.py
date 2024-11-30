# ui/components/rectangle.py

from PIL import ImageDraw
from .base import Component

class Rectangle(Component):
    def __init__(self, x, y, width, height, style=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.style = style or {}
        self.children = []

    def add_child(self, child: Component):
        self.children.append(child)

    def render(self, draw: ImageDraw):
        fill = self.style.get("background", 255)  # Default background: white
        outline = self.style.get("border", None)
        draw.rectangle(
            [self.x, self.y, self.x + self.width, self.y + self.height],
            fill=fill,
            outline=outline,
        )
        for child in self.children:
            child.render(draw)
