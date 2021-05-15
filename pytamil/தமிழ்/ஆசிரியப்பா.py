# -*- coding: utf-8 -*-

import sys
import antlr4
from antlr4 import *
from antlr4.tree.Trees import Trees
import os

# from codegen import codegen
from pytamil.தமிழ்.codegen.ஆசிரியப்பாLexer import ஆசிரியப்பாLexer
from pytamil.தமிழ்.codegen.ஆசிரியப்பாParser import ஆசிரியப்பாParser
from codecs import open


def gettree(பாடல்):
    input_stream = antlr4.InputStream(பாடல்)
    lexer = ஆசிரியப்பாLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ஆசிரியப்பாParser(stream)
    tree = parser.ஆசிரியப்பா()
    return tree, parser

def சீர்_வாய்பாடு_கொடு(பாடல்):
    
   
    tree, parser = gettree(பாடல்)
    
    அடிவரிசை =[]
    அடிகள் = tree.children[0].children
    for அடி in அடிகள்:
        சீர்கள் = அடி.children
        சீர்_வாய்பாடு_வரிசை = [parser.ruleNames[சீர்.children[0].children[0].getRuleIndex()] for சீர் in சீர்கள் if சீர்.getChildCount() != 0]
        அடிவரிசை.append(சீர்_வாய்பாடு_வரிசை)

    return அடிவரிசை