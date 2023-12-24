import logging
from pynput import mouse
import pyautogui


def press_e():
    pyautogui.press('e')


def press_q():
    pyautogui.press('q')


class MouseListener:
    # config is optional
    def __init__(self, config=None):
        self.held_buttons = set()

        if config['left'] == config['right']:
            raise Exception("Left and right buttons cannot be the same")

        if config is None:
            config = {"left": "Button.button9", "right": "Button.button8"}

        self.button_actions = {
            config['left']: press_e,
            config['right']: press_q
        }
        self.listener = mouse.Listener(on_click=self.on_click)

    def on_click(self, x, y, button, pressed):
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
        self.listener.start()

    def join(self):
        self.listener.join()
