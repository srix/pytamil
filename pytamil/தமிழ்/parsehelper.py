# -*- coding: utf-8 -*-
"""
parsehelper — shared ANTLR parse helper.

Every grammar wrapper (சீர், வெண்பா, ஆசிரியப்பா, மாத்திரை, சொல், புணர்ச்சிவிதிகள்) builds the
same InputStream → Lexer → CommonTokenStream → Parser chain. This module does it once and,
unlike the generated defaults, collects lexer and parser errors as data instead of printing
them to stderr and silently returning a garbled tree.

    result = parse(சீர்Lexer, சீர்Parser, 'சீர்', 'வானினும்')
    result.tree      # parse tree (ParserRuleContext)
    result.parser    # the parser, for ruleNames etc.
    result.errors    # list[ParseError], empty when the input parsed cleanly

With strict=True a non-empty error list raises ParseFailed instead.
"""
from dataclasses import dataclass, field
from typing import Any, List

import antlr4
from antlr4.error.ErrorListener import ErrorListener


@dataclass(frozen=True)
class ParseError:
    """One syntax error reported by the lexer or the parser."""
    line: int         # 1-based line
    column: int       # 0-based column, as ANTLR reports it
    message: str      # ANTLR's message
    stage: str        # 'lexer' or 'parser'

    def __str__(self):
        return f"{self.stage} {self.line}:{self.column} {self.message}"


class ParseFailed(Exception):
    """Raised by parse(..., strict=True) when the input does not parse cleanly."""

    def __init__(self, errors: List[ParseError]):
        self.errors = list(errors)
        super().__init__("; ".join(str(e) for e in self.errors))


@dataclass
class ParseResult:
    """Result of parse()."""
    tree: Any
    parser: antlr4.Parser
    errors: List[ParseError] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        """True when the input parsed with no errors."""
        return not self.errors


class ErrorCollector(ErrorListener):
    """Collects syntax errors; never raises, never prints."""

    def __init__(self, stage: str, errors: List[ParseError]):
        super().__init__()
        self.stage = stage
        self.errors = errors

    # Signature is fixed by ANTLR's ErrorListener interface; it cannot be changed.
    # pylint: disable-next=too-many-arguments,too-many-positional-arguments
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(ParseError(line, column, msg, self.stage))


def parse(LexerCls, ParserCls, start_rule: str, text: str, *,
          strict: bool = False) -> ParseResult:
    """
    Parse `text` with the given generated Lexer/Parser classes, starting at `start_rule`.

    Errors from both the lexer and the parser are collected on the returned ParseResult.
    With strict=True, any error raises ParseFailed.
    """
    errors: List[ParseError] = []

    lexer = LexerCls(antlr4.InputStream(text))
    lexer.removeErrorListeners()
    lexer.addErrorListener(ErrorCollector('lexer', errors))

    parser = ParserCls(antlr4.CommonTokenStream(lexer))
    parser.removeErrorListeners()
    parser.addErrorListener(ErrorCollector('parser', errors))

    tree = getattr(parser, start_rule)()

    if strict and errors:
        raise ParseFailed(errors)
    return ParseResult(tree, parser, errors)
