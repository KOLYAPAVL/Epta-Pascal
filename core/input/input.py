from __future__ import annotations

from typing import Dict, Any, List

import os

from core.input.entity import InputEntity
from core.input.dto import InputResult, InputFile, InputArguments
from exceptions import PathIncorrect, IncorrectExt
from config.enum import EXTENSIONAL


class InputProcess:

    def __init__(self, arguments: Dict[str, Any]) -> None:
        self.arguments: InputEntity = InputEntity(**arguments)

    @staticmethod
    def _get_lines(path: str) -> List[str]:
        lines: List[str] = list()
        with open(path, "r") as file:
            for line in file.read().split("\n"):
                lines.append(line)
        return lines

    def _get_file_info(self) -> InputFile:
        file_path: str = self.arguments.path
        if not os.path.isfile(file_path):
            raise PathIncorrect()

        _path, ext = os.path.splitext(file_path)
        if ext != EXTENSIONAL:
            raise IncorrectExt()

        return InputFile(
            lines=self._get_lines(file_path),
            file_name=_path.split("/")[-1],
            file_ext=ext,
            file_path=file_path,
        )

    def _get_arguments(self) -> InputArguments:
        return InputArguments(
            builds_path=self.arguments.builds_path,
            clear_builds=self.arguments.clear_builds,
            system=self.arguments.system,
        )

    def execute(self) -> InputResult:
        return InputResult(
            file=self._get_file_info(),
            arguments=self._get_arguments(),
        )
