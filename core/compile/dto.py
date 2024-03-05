from __future__ import annotations

from typing import TypedDict, List


class CompiledResult(TypedDict):
    lines: List[str]
    string: str
