from __future__ import annotations

from typing import List, Any, Optional

from config.errors import Errors


class BaseModuleException(Exception):
    with_format: bool = False
    err: str = ""

    def __init__(self, formats: Optional[List[Any]] = None, *args) -> None:
        print(formats)
        if self.with_format and formats:
            err = self.err.format(*formats)
        else:
            err = self.err
        super().__init__(err, *args)


class ArgumentNotFound(BaseModuleException):
    with_format: bool = True
    err: str = Errors.arg_not_found


class PathArgumentNotFound(BaseModuleException):
    err: str = Errors.file_path_argument_not_found


class UnknownSystem(BaseModuleException):
    with_format: bool = True
    err: str = Errors.unknown_system


class PathIncorrect(BaseModuleException):
    err: str = Errors.file_path_not_found


class IncorrectExt(BaseModuleException):
    err: str = Errors.file_ext_incorrect


class BuildPathDoesNotExists(BaseModuleException):
    err: str = Errors.build_path_not_found
