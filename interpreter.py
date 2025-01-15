import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pydantic import BaseModel

from utils.rich_logging import logger as log
from utils.constants import ReservedKeyword


class ThoCommand(BaseModel):
    order: int
    command: str
    value: float
    operation: str


class AskThoCommand(BaseModel):
    order: int
    var_name: str
    value: float


class ThoInterpreter:
    def __init__(self, script_file: str, r: float = 0.0) -> None:
        self.__r = r
        self.__ask_registry = []
        self.__command_registry = []
        self.__script_file = script_file

    @property
    def ask_registry(self) -> list[AskThoCommand]:
        return self.__ask_registry

    @property
    def command_registry(self) -> list[ThoCommand]:
        return self.__command_registry

    @property
    def r(self) -> float:
        return self.__r

    @r.setter
    def r(self, r: float = 0.0) -> None:
        self.__r = r

    @property
    def script_file(self) -> str:
        return self.__script_file

    @script_file.setter
    def script_file(self, script_file: str) -> None:
        if not os.path.isfile(script_file):
            raise FileNotFoundError(f"Provided file {script_file} was not found within /checks.")

        self.__script_file = script_file

    def clear(self) -> None:
        self.__ask_registry.clear()
        self.__command_registry.clear()
        self.__script_file = None
        self.__r = 0.0

    def __upsert_command(self, order: int, command: str, value: float | str, operation: str) -> None:
        try:
            float_value = float(value) if not isinstance(value, float) else value
            self.__command_registry.append(
                ThoCommand(
                    order=order,
                    command=command,
                    value=float_value,
                    operation=operation
                ))

        except ValueError:
            ask_command = next(
                (command for command in self.__ask_registry if command.var_name == value), None)

            if ask_command is None:
                raise ValueError(f"Invalid command provided, not in recorded registry: {command}")

            log.info(f"Found Ask Command: {ask_command}")

            self.__command_registry.append(
                ThoCommand(
                    order=order,
                    command=command,  # NOTE: Empty at First.
                    value=ask_command.value,
                    operation=operation  # NOTE: Empty at First.
                ))

    def __upsert_ask_command(self, order: int, var_name: str, value: float) -> None:
        self.__ask_registry.append(
            AskThoCommand(
                order=order,
                var_name=var_name,
                value=value))

    def __check_is_float(self, value: any) -> float:
        try:
            return float(value)
        except ValueError as e:
            log.error(f"Invalid value, could not convert to float: {e}")
            raise e

    def parse(self) -> None:
        """
        Parses a Tho script file and returns a tuple of two lists:
        list of THO commands and list of AskThoCommands respectively.

        :raises FileNotFoundError: If the script file is not found.
        :raises ValueError: If there is an error in the script file.

        :return: A tuple of two lists: list of THO commands and list of AskThoCommands respectively.
        """
        try:
            if not os.path.isfile(self.__script_file):
                raise FileNotFoundError(f"Provided file {self.__script_file} was not found within /checks/.")

            with open(self.__script_file, "r") as file:
                lines = file.readlines()
                order = 0

                for line in lines:
                    line = line.strip()
                    if not line or line.startswith(ReservedKeyword.COMMENT.value):
                        continue

                    if line.startswith(ReservedKeyword.ASK.value):
                        command, var_name = line.split()
                        user_input = input(f"Enter a value for {var_name}: ")
                        user_input = self.__check_is_float(user_input)

                        self.__upsert_ask_command(
                            order=order,
                            var_name=var_name,
                            value=user_input)
                        order += 1

                    elif any(line.startswith(operation.value) for operation in [
                        ReservedKeyword.ADD,
                        ReservedKeyword.SUB,
                        ReservedKeyword.MUL,
                        ReservedKeyword.DIV
                    ]):
                        command, value = line.split()
                        self.__upsert_command(
                            order=order,
                            command=command,
                            value=value,
                            operation=command)
                        order += 1

                    elif line.startswith(ReservedKeyword.TELL.value):
                        r = self.execute()
                        log.info(f"Result: {r}")
                        break

                    else:
                        log.error(f"Invalid command provided within script: {line}")

        except FileNotFoundError as e:
            log.error(f"Error [{e}]")

        except ValueError as e:
            log.error(f"Error [{e}]")

    def execute(self) -> float:
        """
        Executes the commands in the command registry,
        in order and returns the result or R, after
        all commands have been executed.

        :raises ZeroDivisionError: If the result is zero.
        :raises ValueError: If the result is not a float.

        :return: The result of R after all executed commands.
        """
        self.__command_registry.sort(key=lambda x: x.order)

        try:
            for command in self.__command_registry:
                if command.operation == ReservedKeyword.ADD.value:
                    self.__r += command.value

                    log.info(f"ADD {command.value} to register (R): {self.__r}")

                elif command.operation == ReservedKeyword.SUB.value:
                    self.__r -= command.value

                    log.info(f"SUB {command.value} to register (R): {self.__r}")

                elif command.operation == ReservedKeyword.MUL.value:
                    self.__r *= command.value

                    log.info(f"MUL {command.value} to register (R): {self.__r}")

                elif command.operation == ReservedKeyword.DIV.value:
                    self.__r /= command.value

                    log.info(f"DIV {command.value} to register (R): {self.__r}")

                else:
                    log.error(f"Unknown operation provided: {command.operation}")
                    break

        except ZeroDivisionError as e:
            log.error(f"Error [{e}]")

        except ValueError as e:
            log.error(f"Error [{e}]")

        return self.__r
