# -*- coding: utf-8 -*-

import sys
import antlr4
from antlr4 import *
from antlr4.tree.Trees import Trees
import os

# from codegen import codegen
from pytamil.தமிழ்.codegen.சீர்Lexer import சீர்Lexer
from pytamil.தமிழ்.codegen.சீர்Parser import சீர்Parser
from pytamil.தமிழ் import பாகுபடுத்தி
from codecs import open


def gettree(பதம்):
    பா = பாகுபடுத்தி.மரம்_கொடு(சீர்Lexer, சீர்Parser, 'சீர்', பதம்)
    return பா.மரம், பா.parser

def சீர்_வாய்பாடு_கொடு(பதம்):
    tree, parser = gettree(பதம்)
    சீர்_வாய்பாடு = parser.ruleNames[tree.children[0].children[0].getRuleIndex()]
    
    return சீர்_வாய்பாடு