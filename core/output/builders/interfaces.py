from __future__ import annotations

from abc import ABC, abstractmethod


class IBuilder(ABC):

    @staticmethod
    @abstractmethod
    def build(file_path: str) -> None:
        ...

    @staticmethod
    @abstractmethod
    def run(file_path: str) -> None:
        ...
