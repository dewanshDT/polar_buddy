# ui/components/tab_bar.py

from PIL import ImageDraw
from .base import Component

class TabBar(Component):
    def __init__(self, x, y, width, height, tabs, active_index, font, style=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.tabs = tabs
        self.active_index = active_index
        self.font = font
        self.style = style or {}

    def render(self, draw: ImageDraw):
        tab_width = self.width // len(self.tabs)
        for i, tab in enumerate(self.tabs):
            x0 = self.x + i * tab_width
            y0 = self.y
            x1 = x0 + tab_width
            y1 = y0 + self.height

            if i == self.active_index:
                fill = self.style.get("active_background", 0)  # Active tab background: black
                text_fill = self.style.get("active_color", 255)  # Active tab text: white
            else:
                fill = self.style.get("background", 255)  # Inactive tab background: white
                text_fill = self.style.get("color", 0)  # Inactive tab text: black

            draw.rectangle([x0, y0, x1, y1], fill=fill)
            w, h = draw.textsize(tab, font=self.font)
            text_x = x0 + (tab_width - w) / 2
            text_y = y0 + (self.height - h) / 2
            draw.text((text_x, text_y), tab, font=self.font, fill=text_fill)
