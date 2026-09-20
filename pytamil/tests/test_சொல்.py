# -*- coding: utf-8 -*-
"""
Tests for the சொல் (word phonotactics) grammar, resources/சொல்.g4.

A word is "accepted" when the parser reports zero syntax errors. The expectations below
were checked against the grammar on 2026-09-20. Cases marked xfail are known gaps in the
grammar (ordinary words it rejects, malformed words it accepts); they are tracked in
specs/2026-09-20-revival-and-roadmap.md (Backlog: சொல்.g4).
"""
import pytest
from pytamil.தமிழ் import சொல்

GRAMMAR_GAP = "சொல்.g4 gap, see specs/2026-09-20-revival-and-roadmap.md Backlog"


def _பிழைகள்(சொல்_உரை):
    tree, parser = சொல்.get_soll_tree(சொல்_உரை)
    return parser.getNumberOfSyntaxErrors()


@pytest.mark.parametrize("சொல்_உரை", [
    "அம்மா",        # உயிர் முதல், உடன்நிலை மெய்ம்மயக்கம் ம்ம்
    "கண்ணாடி",      # ண்ண்
    "பூ",           # ஓரெழுத்து
    "தேன்மழை",      # ன்ம் வேற்றுநிலை மெய்ம்மயக்கம்
    "பூக்கள்",      # க்க், ள் ஈறு
    # ordinary words the grammar currently rejects
    pytest.param("தமிழ்",   marks=pytest.mark.xfail(reason=GRAMMAR_GAP, strict=True)),
    pytest.param("வணக்கம்", marks=pytest.mark.xfail(reason=GRAMMAR_GAP, strict=True)),
    pytest.param("மரம்",    marks=pytest.mark.xfail(reason=GRAMMAR_GAP, strict=True)),
    pytest.param("கண்",     marks=pytest.mark.xfail(reason=GRAMMAR_GAP, strict=True)),
    pytest.param("மீன்",    marks=pytest.mark.xfail(reason=GRAMMAR_GAP, strict=True)),
    pytest.param("ஆஅ",      marks=pytest.mark.xfail(reason=GRAMMAR_GAP + " (உயிரளபெடை)", strict=True)),
])
def test_சரியான_சொல்(சொல்_உரை):
    assert _பிழைகள்(சொல்_உரை) == 0


@pytest.mark.parametrize("சொல்_உரை", [
    "ரம்மா", "லம்மா", "ழம்மா", "ளம்மா",   # ர ல ழ ள cannot begin a word
    "யெம்மா",                              # ய + எ cannot begin a word
    "கத்ர்", "கச்ச்", "கட்ட்", "கப்ப்", "கரற்",  # த் ச் ட் ப் ற் cannot end a word
    "கண்ர்", "மன்ர்", "பன்ழ்",              # invalid மெய்ம்மயக்கம்
    # malformed words the grammar currently accepts
    pytest.param("ஙெம்மா", marks=pytest.mark.xfail(reason=GRAMMAR_GAP, strict=True)),
    pytest.param("ஞெம்மா", marks=pytest.mark.xfail(reason=GRAMMAR_GAP, strict=True)),
    pytest.param("வெம்மா", marks=pytest.mark.xfail(reason=GRAMMAR_GAP, strict=True)),
])
def test_தவறான_சொல்(சொல்_உரை):
    assert _பிழைகள்(சொல்_உரை) > 0


def test_print_soll_tree_shape():
    tree, parser = சொல்.get_soll_tree("அம்மா")
    assert tree.toStringTree(recog=parser).startswith("(சொல் (பொதுமொழி (மொழிமுதல் (உயிர்க்குறில் அ))")
