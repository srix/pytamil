# -*- coding: utf-8 -*-
"""
சீர் — ஒரு பதத்தின் சீர் வாய்பாட்டை (தேமா, புளிமாங்காய் ...) அறியும் கூறு.

    சீர்_வாய்பாடு_கொடு('வானினும்')   # 'கூவிளம்'

அசைப் பாகுபாடு resources/சீர்.g4 இலக்கணத்தால்; வாய்பாட்டுப் பெயர் அந்த இலக்கண விதியின்
பெயரே. வெண்பா, ஆசிரியப்பா இரண்டும் இதே இலக்கணத்தையே (import சீர்) பயன்படுத்துகின்றன.
"""
from pytamil.தமிழ் import பாகுபடுத்தி
from pytamil.தமிழ்.codegen.சீர்Lexer import சீர்Lexer
from pytamil.தமிழ்.codegen.சீர்Parser import சீர்Parser


def gettree(பதம்):
    """Parse a பதம் with the சீர் grammar; returns (tree, parser)."""
    பா = பாகுபடுத்தி.மரம்_கொடு(சீர்Lexer, சீர்Parser, 'சீர்', பதம்)
    return பா.மரம், பா.parser

def சீர்_வாய்பாடு_கொடு(பதம்):
    """பதத்தின் சீர் வாய்பாட்டுப் பெயர் (எ.கா. 'கூவிளம்')."""
    tree, parser = gettree(பதம்)
    சீர்_வாய்பாடு = parser.ruleNames[tree.children[0].children[0].getRuleIndex()]

    return சீர்_வாய்பாடு
