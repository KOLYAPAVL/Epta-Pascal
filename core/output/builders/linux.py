from __future__ import annotations

import os
import subprocess

from core.output.builders.interfaces import IBuilder


class LinuxBuilder(IBuilder):

    @staticmethod
    def build(file_path: str) -> None:
        subprocess.call(["pc", file_path], stdout=subprocess.PIPE)

    @staticmethod
    def run(file_path: str) -> None:
        file_path = file_path.replace(".pas", "")
        os.system(f"{file_path}")
