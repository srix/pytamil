# -*- coding: utf-8 -*-
"""
பாகுபடுத்தி — shared ANTLR parse helper.

Every grammar wrapper (சீர், வெண்பா, ஆசிரியப்பா, மாத்திரை, சொல், புணர்ச்சிவிதிகள்) builds the
same InputStream → Lexer → CommonTokenStream → Parser chain. This module does it once and,
unlike the generated defaults, collects lexer and parser errors as data instead of printing
them to stderr and silently returning a garbled tree.

    பா = மரம்_கொடு(சீர்Lexer, சீர்Parser, 'சீர்', 'வானினும்')
    பா.மரம்      # parse tree (ParserRuleContext)
    பா.parser    # the parser, for ruleNames etc.
    பா.பிழைகள்   # list[பாகுபாட்டுப்பிழை], empty when the input parsed cleanly

With கண்டிப்பு=True a non-empty error list raises பாகுபாட்டுவிதிவிலக்கு instead.
"""
from dataclasses import dataclass, field
from typing import Any, List

import antlr4
from antlr4.error.ErrorListener import ErrorListener


@dataclass(frozen=True)
class பாகுபாட்டுப்பிழை:
    """One syntax error reported by the lexer or the parser."""
    வரி: int          # 1-based line
    நெடுக்கை: int     # 0-based column, as ANTLR reports it
    செய்தி: str       # ANTLR's message
    நிலை: str         # 'lexer' or 'parser'

    def __str__(self):
        return f"{self.நிலை} {self.வரி}:{self.நெடுக்கை} {self.செய்தி}"


class பாகுபாட்டுவிதிவிலக்கு(Exception):
    """Raised by மரம்_கொடு(..., கண்டிப்பு=True) when the input does not parse cleanly."""

    def __init__(self, பிழைகள்: List[பாகுபாட்டுப்பிழை]):
        self.பிழைகள் = list(பிழைகள்)
        super().__init__("; ".join(str(ப) for ப in self.பிழைகள்))


@dataclass
class பாகுபாடு:
    """Result of மரம்_கொடு."""
    மரம்: Any
    parser: antlr4.Parser
    பிழைகள்: List[பாகுபாட்டுப்பிழை] = field(default_factory=list)

    @property
    def சரியா(self) -> bool:
        return not self.பிழைகள்


class பிழைசேகரிப்பான்(ErrorListener):
    """Collects syntax errors; never raises, never prints."""

    def __init__(self, நிலை: str, பிழைகள்: List[பாகுபாட்டுப்பிழை]):
        super().__init__()
        self.நிலை = நிலை
        self.பிழைகள் = பிழைகள்

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.பிழைகள்.append(பாகுபாட்டுப்பிழை(line, column, msg, self.நிலை))


def மரம்_கொடு(LexerCls, ParserCls, தொடக்கவிதி: str, உரை: str, *, கண்டிப்பு: bool = False) -> பாகுபாடு:
    """
    Parse `உரை` with the given generated Lexer/Parser classes, starting at rule `தொடக்கவிதி`.

    Errors from both the lexer and the parser are collected on the returned பாகுபாடு.
    With கண்டிப்பு=True, any error raises பாகுபாட்டுவிதிவிலக்கு.
    """
    பிழைகள்: List[பாகுபாட்டுப்பிழை] = []

    lexer = LexerCls(antlr4.InputStream(உரை))
    lexer.removeErrorListeners()
    lexer.addErrorListener(பிழைசேகரிப்பான்('lexer', பிழைகள்))

    parser = ParserCls(antlr4.CommonTokenStream(lexer))
    parser.removeErrorListeners()
    parser.addErrorListener(பிழைசேகரிப்பான்('parser', பிழைகள்))

    மரம் = getattr(parser, தொடக்கவிதி)()

    if கண்டிப்பு and பிழைகள்:
        raise பாகுபாட்டுவிதிவிலக்கு(பிழைகள்)
    return பாகுபாடு(மரம், parser, பிழைகள்)
