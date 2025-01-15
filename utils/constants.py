import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from enum import Enum
from rich_logging import logger as log


class ReservedKeyword(str, Enum):
    ADD = "ADD"
    SUB = "SUB"
    MUL = "MUL"
    DIV = "DIV"
    ASK = "ASK"
    TELL = "TELL"
    COMMENT = "#"


def check_constants() -> None:
    log.info(f"""
    Constants:
    RESERVED_KEYWORDS = {",".join(ReservedKeyword.__members__)}
    """)
