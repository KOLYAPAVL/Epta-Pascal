from __future__ import annotations

from typing import List

from core.compile.dto import CompiledResult


# FIXME: Need refactoring
class CompileProcess:
    splitters: List = [' ', '(', ':', ';']

    def __init__(self, lines: List[str]) -> None:
        self.lines: List[str] = lines

    @staticmethod
    def process_word(word: str) -> str:
        match word:
            case "дичь":
                return "program"
            case "запомнинах":
                return "var"
            case "число":
                return "integer"
            case "строчечка":
                return "string"
            case "погнали":
                return "begin"
            case "нахуй":
                return "end"
            case "нахуй.":
                return "end."
            case "соберинахспробелом":
                return "readLn"
            case "вывединахспробелом":
                return "writeLn"
            case _:
                return word

    def process_line(self, s: str) -> str:
        pascal_string: str = ""
        code_word: str = ""
        i: int = 0
        while i < len(s):
            if s[i] in self.splitters:
                pascal_string += (self.process_word(code_word) + s[i])
                code_word = ""
            else:
                code_word += s[i]
            i += 1
        pascal_string += self.process_word(code_word)
        return pascal_string

    def execute(self) -> CompiledResult:
        new_lines: List[str] = list()
        for line in self.lines:
            new_lines.append(self.process_line(line))

        return CompiledResult(
            lines=new_lines,
            string="\n".join(new_lines),
        )
