# -*- coding: utf-8 -*-

import sys
import antlr4
from antlr4 import *
from antlr4.tree.Trees import Trees
import os

# from codegen import codegen
from pytamil.தமிழ்.codegen.வெண்பாLexer import வெண்பாLexer
from pytamil.தமிழ்.codegen.வெண்பாParser import வெண்பாParser
from pytamil.தமிழ் import பாகுபடுத்தி
from codecs import open

# nltk is imported lazily inside the tree-drawing helpers below, so that
# importing this module for analysis does not require the visualisation stack.


def gettree(பாடல்):
    பா = பாகுபடுத்தி.மரம்_கொடு(வெண்பாLexer, வெண்பாParser, 'வெண்பா', பாடல்)
    return பா.மரம், பா.parser

def சீர்கொடு(பாடல்):
    
   
    tree, parser = gettree(பாடல்)
    
    அடிவரிசை =[]
    அடிகள் = tree.children[0].children
    for அடி in அடிகள்:
        சீர்கள் = அடி.children
        சீர்வரிசை = [parser.ruleNames[சீர்.children[0].getRuleIndex()] for சீர் in சீர்கள் if சீர்.getChildCount() != 0]
        அடிவரிசை.append(சீர்வரிசை)

    return அடிவரிசை

    
    


def saveas_txttree(tree, parser, outfilename):
    from nltk import Tree as nltkTree
    try:
        from nltk.tree import TreePrettyPrinter
    except ImportError:  # nltk < 3.8
        from nltk.treeprettyprinter import TreePrettyPrinter

    strtree = Trees.toStringTree(tree, None, parser)
    t = nltkTree.fromstring(strtree)
    a = TreePrettyPrinter(t).text()

    with open(outfilename + ".txt", 'w', encoding='utf8') as f:
        f.write( a)
    return a

def saveas_pngtree(tree, parser, outfilename):
    # Image output of the parse tree is not implemented yet; see specs/2026-09-20-revival-and-roadmap.md (Phase 2d, மரம்காட்டு).
    raise NotImplementedError("PNG/SVG tree output is not implemented; use saveas_txttree")


def main():
    infilename = os.path.join(os.path.dirname(__file__),'../debug/வெண்பா-input.txt')
    outfilename = os.path.join(os.path.dirname(__file__),'../debug/வெண்பா-output')
    பாடல் = open(infilename).read()   
    tree , parser = gettree(பாடல்)
    saveas_txttree(tree,parser,outfilename)
    #saveas_pngtree(tree,parser,outfilename)
    சீர்கொடு(பாடல்)

if __name__ == '__main__':
    main()
