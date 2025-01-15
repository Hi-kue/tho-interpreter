import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "utils")))

from interpreter import ThoInterpreter
from utils.rich_logging import logger as log


DEFAULT_SCRIPT_PATH = os.path.join(os.path.dirname(__file__), "checks")


def main() -> None:
    while True:
        log.info("Enter a valid file within /checks/ to run (or 'exit' to exit): ")
        file_name = input()

        if file_name == "exit":
            break

        interpreter = ThoInterpreter(script_file=f"{DEFAULT_SCRIPT_PATH}/{file_name}")
        interpreter.parse()

        log.info(f"Command Registry: {interpreter.command_registry}")
        log.info(f"Ask Registry: {interpreter.ask_registry}")


if __name__ == "__main__":
    main()
