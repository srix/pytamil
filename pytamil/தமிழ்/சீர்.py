# -*- coding: utf-8 -*-

import sys
import antlr4
from antlr4 import *
from antlr4.tree.Trees import Trees
import os

# from codegen import codegen
from pytamil.தமிழ்.codegen.சீர்Lexer import சீர்Lexer
from pytamil.தமிழ்.codegen.சீர்Parser import சீர்Parser
from codecs import open


def gettree(பதம்):
    input_stream = antlr4.InputStream(பதம்)
    lexer = சீர்Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = சீர்Parser(stream)
    tree = parser.சீர்()

    return tree, parser

def சீர்_வாய்பாடு_கொடு(பதம்):
    tree, parser = gettree(பதம்)
    சீர்_வாய்பாடு = parser.ruleNames[tree.children[0].children[0].getRuleIndex()]
    
    return சீர்_வாய்பாடு