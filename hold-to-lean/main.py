import argparse
import logging
import json


def config():
    import config_helper
    config_helper.main()


def not_config():
    from mouse_listener import MouseListener

    listener = MouseListener(config)
    listener.start()
    listener.join()


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument("--config", action="store_true", help="Launch configuration helper")
    args = parser.parse_args()

    if args.config:
        config()

    else:
        try:
            with open('config.json', 'r') as f:
                config = json.loads(f.read())
                f.close()

            logging.info("Configuration file found!")
            not_config()

        except FileNotFoundError:
            logging.error("Configuration file not found! Taking you to the configuration helper.")
            config()


