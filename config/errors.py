from __future__ import annotations


class Errors:
    file_path_argument_not_found: str = "Argument --path not found"
    file_path_not_found: str = "Path to .epas file not found"
    file_ext_incorrect: str = "Incorrect extensional of file in --path argument"
    arg_not_found: str = "Argument {} not found"
    unknown_system: str = "System {} not found"
    build_path_not_found: str = "Build path {} does not exists"
