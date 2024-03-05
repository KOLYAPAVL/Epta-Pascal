from __future__ import annotations

from dataclasses import dataclass

"""
Arguments of command line to process compiling
"""


@dataclass(kw_only=True)
class InputEntity:
    path: str  # Path to .epas file
    builds_path: str  # Path to build directory
    clear_builds: bool  # Need to clear build directory
    system: str  # System name
