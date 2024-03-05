from __future__ import annotations

from typing import List, Any, Dict, TYPE_CHECKING

import sys
import os

from arguments import Arguments, Argument
from exceptions import PathArgumentNotFound, UnknownSystem
from config.enum import SystemsEnum

from core.input.input import InputProcess
from core.compile.compile import CompileProcess
from core.output.output import OutputProcess

if TYPE_CHECKING:
    from core.input.dto import InputResult
    from core.compile.dto import CompiledResult


def str_cleaner(value: Any) -> str:
    return str(value)


def bool_cleaner(value: Any) -> bool:
    return value in ["1", "true", "True"]


def builds_cleaner(value: Any) -> str:
    val = str(value)
    if val[-1] != "/":
        val += "/"
    return val


def system_cleaner(value: Any) -> SystemsEnum:
    value = value.lower().title()
    if not hasattr(SystemsEnum, value):
        raise UnknownSystem([value])
    return getattr(SystemsEnum, value)


arguments_config = Arguments(
    Argument(
        name="path",
        position=0,
        required=True,
        required_exception_class=PathArgumentNotFound,
        clean_func=str_cleaner,
    ),
    Argument(
        name="builds_path",
        position=1,
        required=False,
        clean_func=str_cleaner,
        default=os.path.dirname(os.path.realpath(__file__))+"/builds/",
    ),
    Argument(
        name="clear_builds",
        position=2,
        required=False,
        clean_func=bool_cleaner,
        default=False,
    ),
    Argument(
        name="system",
        position=3,
        required=False,
        clean_func=system_cleaner,
        default=SystemsEnum.Windows,
    )
)


def parse_arguments() -> Dict[str, Any]:
    """Parsing all arguments"""
    arguments: List[str] = sys.argv[1:]
    result: Dict[str, Any] = arguments_config.execute(arguments)
    return result


def run() -> None:
    arguments: Dict[str, Any] = parse_arguments()
    input_result: InputResult = InputProcess(arguments).execute()
    compiled_result: CompiledResult = CompileProcess(input_result["file"]["lines"]).execute()
    OutputProcess(input_result, compiled_result).execute()


if __name__ == "__main__":
    run()
