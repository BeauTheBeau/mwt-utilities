from pynput import mouse
import logging
import json


class ButtonListener:
    def __init__(self):
        self.buttons = {}
        self.current_button = None
        self.listener = mouse.Listener(on_click=self.on_click)

    def on_click(self, x, y, button, pressed):
        if pressed:
            print(f"\tButton pressed: {button}")
            self.current_button = button
            self.listener.stop()

    def start(self):
        self.listener.start()

    def join(self):
        self.listener.join()

    def get_buttons(self):
        return self.buttons


def main():
    logging.basicConfig(level=logging.INFO)
    listener = ButtonListener()

    for direction in ["right", "left"]:
        print(f"\nWhat button do you want to use to lean {direction}?")
        listener.start()
        listener.join()
        listener.buttons[direction] = listener.current_button
        listener.listener = mouse.Listener(on_click=listener.on_click)

    print()

    buttons = listener.get_buttons()
    for button in buttons:
        buttons[button] = str(buttons[button])
        print(f"Button for {button} is {buttons[button]}")

    # Write to config file
    with open("config.json", "w") as f:
        f.write(json.dumps(buttons, indent=4))
        f.close()

    print("\nConfiguration saved to config.json")
    print("You're good to go!")


if __name__ == "__main__":
    main()
