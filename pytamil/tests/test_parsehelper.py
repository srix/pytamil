# -*- coding: utf-8 -*-
"""parsehelper tests: syntax errors are collected as data instead of printed."""
import pytest

from pytamil.தமிழ் import parsehelper
from pytamil.தமிழ்.codegen.சீர்Lexer import சீர்Lexer
from pytamil.தமிழ்.codegen.சீர்Parser import சீர்Parser


def test_clean_input_has_no_errors():
    result = parsehelper.parse(சீர்Lexer, சீர்Parser, 'சீர்', 'வானினும்')
    assert result.errors == []
    assert result.ok
    assert result.parser.ruleNames[result.tree.getRuleIndex()] == 'சீர்'
    assert result.tree.getText() == 'வானினும்<EOF>'   # start rule ends with EOF


def test_bad_input_errors_are_collected(capsys):
    # 'x' is not a token of the சீர் grammar: a lexer error at line 1, column 9 (0-based).
    result = parsehelper.parse(சீர்Lexer, சீர்Parser, 'சீர்', 'தண்மையும்xx')
    assert result.errors, "expected at least one error"
    first = result.errors[0]
    assert (first.line, first.column, first.stage) == (1, 9, 'lexer')
    assert 'x' in first.message
    # nothing leaks to stderr: the default ConsoleErrorListener is removed
    assert capsys.readouterr().err == ''
    # a tree is still returned so callers can inspect partial results
    assert result.tree is not None


def test_strict_raises():
    with pytest.raises(parsehelper.ParseFailed) as info:
        parsehelper.parse(சீர்Lexer, சீர்Parser, 'சீர்', 'தண்மையும்xx', strict=True)
    assert info.value.errors[0].stage == 'lexer'
    assert 'தண்மையும்xx' not in str(info.value)  # message describes the error, not the whole input
    assert '1:9' in str(info.value)


def test_strict_passes_on_clean_input():
    result = parsehelper.parse(சீர்Lexer, சீர்Parser, 'சீர்', 'வானினும்', strict=True)
    assert result.errors == []
