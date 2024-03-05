from __future__ import annotations

from typing import Any, List, Optional, Dict

from exceptions import ArgumentNotFound


class Argument:
    name: str
    position: int
    required: bool
    required_exception_class: Any
    default: Any
    clean_func: Any

    def __init__(
        self, name: str, position: int, required: bool, clean_func: Any,
        required_exception_class: Any = None, default: Any = None,
    ) -> None:
        self.name: str = name
        self.position: int = position
        self.required: bool = required
        self.required_exception_class: Any = required_exception_class
        self.default: Any = default
        self.clean_func: Any = clean_func


class Arguments:

    _args_sorted: Optional[List[Argument]] = None
    _args_by_name: Optional[Dict[str, Argument]] = None

    def __init__(self, *args: Argument) -> None:
        self.arguments: tuple[Argument, ...] = args

    @property
    def arguments_sorted(self) -> List[Argument]:
        if self._args_sorted is None:
            self._args_sorted = list(sorted(self.arguments, key=lambda a: a.position))
        return self._args_sorted

    @property
    def arguments_by_name(self) -> Dict[str, Argument]:
        if self._args_by_name is None:
            self._args_by_name = dict()
            for argument in self.arguments:
                self._args_by_name.update({
                    argument.name: argument
                })
        return self._args_by_name

    def execute(self, args: List[str]) -> Dict[str, Any]:
        result: Dict[str, Any] = dict()
        position: int = 0

        # Parse All Arguments
        for arg in args:
            _split: List[str] = arg.split("=")
            _length: int = len(_split)
            if _length == 2:
                name: str = _split[0].replace("--", "")
                value: str = _split[1]
                if name not in self.arguments_by_name:
                    raise ArgumentNotFound([name])
                result[name] = self.arguments_by_name[name].clean_func(value)
            elif _length == 1:
                name: str = self.arguments_sorted[position].name
                value: str = _split[0]
                result[name] = self.arguments_sorted[position].clean_func(value)

            position += 1

        # Add Default
        for name in self.arguments_by_name:
            if name not in result and self.arguments_by_name[name].default is not None:
                result[name] = self.arguments_by_name[name].default

        # Validate Required
        for name in self.arguments_by_name:
            if name not in result and self.arguments_by_name[name].required:
                raise self.arguments_by_name[name].required_exception_class()

        return result
