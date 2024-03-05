from __future__ import annotations

from typing import TypedDict, List


class InputFile(TypedDict):
    lines: List[str]
    file_name: str
    file_ext: str
    file_path: str


class InputArguments(TypedDict):
    builds_path: str
    clear_builds: bool
    system: str


class InputResult(TypedDict):
    file: InputFile
    arguments: InputArguments
