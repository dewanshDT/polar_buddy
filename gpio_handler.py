# gpio_handler.py

import RPi.GPIO as GPIO
import data

class GPIOHandler:
    def __init__(self, state, render_callback):
        self.state = state
        self.render_callback = render_callback

        GPIO.setmode(GPIO.BCM)
        self.BUTTON_NEXT_TAB = 17  # Pin for switching tabs
        self.BUTTON_SCROLL = 27    # Pin for scrolling

        GPIO.setup(self.BUTTON_NEXT_TAB, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.BUTTON_SCROLL, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.add_event_detect(self.BUTTON_NEXT_TAB, GPIO.FALLING, callback=self.next_tab, bouncetime=300)
        GPIO.add_event_detect(self.BUTTON_SCROLL, GPIO.FALLING, callback=self.scroll_list, bouncetime=300)

    def next_tab(self, channel):
        self.state['active_tab'] = (self.state['active_tab'] + 1) % 3
        self.state['scroll_offset'] = 0  # Reset scroll offset
        self.render_callback()

    def scroll_list(self, channel):
        if self.state['active_tab'] == 0:  # Only scroll in "Tasks" tab
            tasks = data.get_tasks()
            max_offset = max(0, len(tasks) - 5)
            if self.state['scroll_offset'] < max_offset:
                self.state['scroll_offset'] += 1
            else:
                self.state['scroll_offset'] = 0  # Loop back to top
            self.render_callback()

    def cleanup(self):
        GPIO.cleanup()
