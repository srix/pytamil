# -*- coding: utf-8 -*-
"""பாகுபடுத்தி tests: syntax errors are collected as data instead of printed."""
import pytest
from pytamil.தமிழ் import பாகுபடுத்தி
from pytamil.தமிழ்.codegen.சீர்Lexer import சீர்Lexer
from pytamil.தமிழ்.codegen.சீர்Parser import சீர்Parser


def test_சரியான_உள்ளீடு_பிழையில்லை():
    பா = பாகுபடுத்தி.மரம்_கொடு(சீர்Lexer, சீர்Parser, 'சீர்', 'வானினும்')
    assert பா.பிழைகள் == []
    assert பா.parser.ruleNames[பா.மரம்.getRuleIndex()] == 'சீர்'
    assert பா.மரம்.getText() == 'வானினும்<EOF>'   # start rule ends with EOF


def test_தவறான_உள்ளீடு_பிழைகள்_சேகரிக்கப்படும்(capsys):
    # 'x' is not a token of the சீர் grammar: a lexer error at line 1, column 9 (0-based).
    பா = பாகுபடுத்தி.மரம்_கொடு(சீர்Lexer, சீர்Parser, 'சீர்', 'தண்மையும்xx')
    assert பா.பிழைகள், "expected at least one error"
    முதல் = பா.பிழைகள்[0]
    assert (முதல்.வரி, முதல்.நெடுக்கை, முதல்.நிலை) == (1, 9, 'lexer')
    assert 'x' in முதல்.செய்தி
    # nothing leaks to stderr: the default ConsoleErrorListener is removed
    assert capsys.readouterr().err == ''
    # a tree is still returned so callers can inspect partial results
    assert பா.மரம் is not None


def test_கண்டிப்பு_விதிவிலக்கு():
    with pytest.raises(பாகுபடுத்தி.பாகுபாட்டுவிதிவிலக்கு) as info:
        பாகுபடுத்தி.மரம்_கொடு(சீர்Lexer, சீர்Parser, 'சீர்', 'தண்மையும்xx', கண்டிப்பு=True)
    assert info.value.பிழைகள்[0].நிலை == 'lexer'
    assert 'தண்மையும்xx' not in str(info.value)  # message describes the error, not the whole input
    assert '1:9' in str(info.value)


def test_கண்டிப்பு_சரியான_உள்ளீடு_விதிவிலக்கு_இல்லை():
    பா = பாகுபடுத்தி.மரம்_கொடு(சீர்Lexer, சீர்Parser, 'சீர்', 'வானினும்', கண்டிப்பு=True)
    assert பா.பிழைகள் == []
