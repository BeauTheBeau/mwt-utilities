import time
from threading import Thread
import logging
import pyautogui

from pynput import mouse
from pynput.mouse import Button, Controller as MouseController

def press_e():
    pyautogui.press('e')


def press_q():
    pyautogui.press('q')


class MouseListener:

    def __init__(self, config=None):
        self.held_buttons = set()

        if config['left'] == config['right']:
            raise ValueError("Left and right buttons cannot be the same! Please reconfigure.")

        if config is None:
            config = {"left": "Button.button9", "right": "Button.button8"}

        self.failsafe_active = False
        self.failsafe_thread = Thread(target=self.check_failsafe)
        self.failsafe_thread.daemon = True

        self.button_actions = {
            config['left']: press_e,
            config['right']: press_q,
            'Button.middle': self.activate_failsafe
        }
        self.listener = mouse.Listener(on_click=self.on_click)

    def check_failsafe(self):
        while True:
            time.sleep(0.1)  # Adjust the interval as needed
            if self.failsafe_active:
                logging.warning("Failsafe triggered - Exiting")
                # Perform any necessary cleanup actions here
                break

    def activate_failsafe(self):
        self.failsafe_active = True

    def deactivate_failsafe(self):
        self.failsafe_active = False

    def on_click(self, x, y, button, pressed):
        if self.failsafe_active:
            return
        button = str(button)

        if pressed:
            self.held_buttons.add(button)
            logging.info(f"Held: {button}")

            if button in self.button_actions:
                try:
                    self.button_actions[button]()
                except Exception as e:
                    logging.error(f"Error executing action for {button}: {e}")

        else:
            self.held_buttons.remove(button)
            logging.info(f"\tReleased: {button}")

            if button in self.button_actions:
                try:
                    self.button_actions[button]()
                except Exception as e:
                    logging.error(f"Error executing action for {button}: {e}")

    def start(self):
        self.failsafe_thread.start()
        self.listener.start()

    def join(self):
        self.listener.join()
