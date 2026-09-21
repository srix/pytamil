# -*- coding: utf-8 -*-
"""
ஆசிரியப்பா — ஆசிரியப்பா அடிகளின் சீர் வாய்பாடுகளைத் தரும் கூறு.

    அடிவரிசை = சீர்_வாய்ப்பாடு_கொடு(பாடல்)   # அடிக்கு ஒரு பட்டியல்

அமைப்பு resources/ஆசிரியப்பா.g4 இலக்கணத்தால் (அது சீர்.g4 ஐ import செய்கிறது). ஆசிரியத்தளை
விதிகளைச் சரிபார்க்கும் ஆய்வி இன்னும் இல்லை; வெண்பா.ஆய்வு() போன்ற ஒன்று திட்டத்தில் உள்ளது.
"""
from pytamil.தமிழ் import parsehelper
from pytamil.தமிழ்.codegen.ஆசிரியப்பாLexer import ஆசிரியப்பாLexer
from pytamil.தமிழ்.codegen.ஆசிரியப்பாParser import ஆசிரியப்பாParser


def gettree(பாடல்):
    """Parse a பாடல் with the ஆசிரியப்பா grammar; returns (tree, parser)."""
    result = parsehelper.parse(ஆசிரியப்பாLexer, ஆசிரியப்பாParser, 'ஆசிரியப்பா', பாடல்)
    return result.tree, result.parser

def சீர்_வாய்ப்பாடு_கொடு(பாடல்):
    """பாடலின் ஒவ்வோர் அடிக்கும் அதன் சீர் வாய்பாடுகளின் பட்டியல்."""
    tree, parser = gettree(பாடல்)

    அடிவரிசை = []
    அடிகள் = tree.children[0].children
    for அடி in அடிகள்:
        சீர்கள் = அடி.children
        சீர்_வாய்பாடு_வரிசை = [parser.ruleNames[சீர்.children[0].children[0].getRuleIndex()]
                                for சீர் in சீர்கள் if சீர்.getChildCount() != 0]
        அடிவரிசை.append(சீர்_வாய்பாடு_வரிசை)

    return அடிவரிசை
