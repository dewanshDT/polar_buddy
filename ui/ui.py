# ui/ui.py

from PIL import Image, ImageDraw, ImageFont
from ui.components import Text, Rectangle, TabBar
import data

# Fonts
font_large = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 16)
font_small = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 12)

# Tabs
tabs = ["Tasks", "Stats", "Settings"]

class UI:
    def __init__(self, width, height, state):
        self.width = width
        self.height = height
        self.state = state

    def render(self):
        image = Image.new('1', (self.width, self.height), 255)  # Create a white background
        draw = ImageDraw.Draw(image)

        # Root component
        root = Rectangle(0, 0, self.width, self.height)

        # Tab bar
        tab_bar = TabBar(
            0, 0, self.width, 25, tabs, self.state['active_tab'], font_small,
            style={
                "background": 255,
                "color": 0,
                "active_background": 0,
                "active_color": 255
            }
        )
        root.add_child(tab_bar)

        # Content area
        content = Rectangle(0, 25, self.width, self.height - 25)
        root.add_child(content)

        active_tab_name = tabs[self.state['active_tab']]

        if active_tab_name == "Tasks":
            tasks = data.get_tasks()
            visible_tasks = tasks[self.state['scroll_offset']:self.state['scroll_offset'] + 5]
            y = 5
            for task in visible_tasks:
                task_text = Text(10, y, task, font_small)
                content.add_child(task_text)
                y += 18
        elif active_tab_name == "Stats":
            stats = data.get_stats()
            y = 5
            for key, value in stats.items():
                stat_text = Text(10, y, f"{key.replace('_', ' ').title()}: {value}", font_small)
                content.add_child(stat_text)
                y += 18
        elif active_tab_name == "Settings":
            settings = data.get_settings()
            y = 5
            for key, value in settings.items():
                setting_text = Text(10, y, f"{key.title()}: {value}", font_small)
                content.add_child(setting_text)
                y += 18

        # Render the UI components
        root.render(draw)

        return image
