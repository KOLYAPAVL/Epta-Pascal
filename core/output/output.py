from __future__ import annotations

from typing import TYPE_CHECKING

import os

from datetime import datetime

from config.enum import BUILDS_DT_FORMAT, PROGRAM_NAME, SystemsEnum
from config.text import BUILD_SUCCESS
from exceptions import BuildPathDoesNotExists

from core.output.builders.linux import LinuxBuilder

if TYPE_CHECKING:
    from core.input.dto import InputResult
    from core.compile.dto import CompiledResult


class OutputProcess:
    input_result: InputResult
    compiled_result: CompiledResult

    def __init__(self, input_result: InputResult, compiled_result: CompiledResult) -> None:
        self.input_result: InputResult = input_result
        self.compiled_result: CompiledResult = compiled_result

    def _get_builds_path(self) -> str:
        now_str: str = datetime.now().strftime(BUILDS_DT_FORMAT)
        build_path: str = self.input_result['arguments']['builds_path']
        build_directory: str = f"{build_path}{now_str}/"

        if not os.path.exists(build_path):
            raise BuildPathDoesNotExists()

        os.mkdir(build_directory)

        return f"{build_directory}{PROGRAM_NAME}"

    def _make_builds_file(self, file_path: str) -> None:
        with open(file_path, "w") as file:
            file.write(self.compiled_result["string"])

    @staticmethod
    def _print_build_success(file_path: str) -> None:
        print(BUILD_SUCCESS.format(file_path))

    def _execute_build(self, file_path: str) -> None:
        builders = {
            SystemsEnum.Linux: LinuxBuilder,
        }
        system_name: str = self.input_result["arguments"]["system"]
        if system_name not in builders:
            return

        builders[system_name].build(file_path)
        self._print_build_success(file_path)
        builders[system_name].run(file_path)

    def execute(self) -> None:
        builds_file_path: str = self._get_builds_path()
        self._make_builds_file(builds_file_path)
        self._execute_build(builds_file_path)
