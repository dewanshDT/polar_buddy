# app.py

import time
from waveshare_epd import epd2in13_V2
from ui import UI  # Simplified import
from gpio_handler import GPIOHandler

def main():
    # Initialize the e-ink display
    epd = epd2in13_V2.EPD()
    epd.init()
    epd.Clear(0xFF)

    WIDTH, HEIGHT = epd.height, epd.width

    # Application state
    state = {
        'active_tab': 0,
        'scroll_offset': 0
    }

    # UI instance
    ui = UI(WIDTH, HEIGHT, state)

    # Render function
    def render():
        image = ui.render()
        epd.display(epd.getbuffer(image))

    # Initial render
    render()

    # GPIO Handler
    gpio_handler = GPIOHandler(state, render)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        epd.sleep()
        gpio_handler.cleanup()

if __name__ == '__main__':
    main()
