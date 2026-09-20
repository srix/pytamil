# -*- coding: utf-8 -*-

import itertools
import antlr4
from antlr4 import *
from pytamil.தமிழ் import எழுத்து as எழுத்து
from pytamil.தமிழ்.codegen.சொல்Lexer import சொல்Lexer
from pytamil.தமிழ்.codegen.சொல்Parser import சொல்Parser
from pytamil.தமிழ் import பாகுபடுத்தி

வேற்றுமை_உருபுகள் = ['ஐ', 'ஆல்', 'கு',  'இன்', 'அது', 'கண்']
நிறம் = []
மாதம் = []
பின்னம் = []
திசை = []


# print(len(tamilutf8.get_letters(u'வணக்கம்')))
# print(tamilutf8.reverse_word(u'வணக்கம்'))
# print(tamilutf8.get_letters(u'வணக்கம்'))
# print(tamilutf8.get_words(u'வணக்கம் தமிழகம்'))
# print(tamilutf8.word_intersection(u'வணக்கம்',u'தமிழகம்'))
# print(tamil.numeral.num2tamilstr_american( 50 ))
# தமிழ்.மெல்லினம் = tamilutf8.mellinam_letters
# print( தமிழ்.மெல்லினம் )

def get_soll_tree(text):
    விரிதொடர் = எழுத்து.உயிர்மெய்விரி(text)
    பா = பாகுபடுத்தி.மரம்_கொடு(சொல்Lexer, சொல்Parser, 'சொல்', விரிதொடர்)
    return பா.மரம், பா.parser

def print_soll_tree(text):
    tree, parser = get_soll_tree(text)
    print(tree.toStringTree(recog=parser))

def ast_to_graphviz(tree, parser, graph=None, parent=None, node_id=None):
    # graphviz is optional; import here so that plain parsing works without it.
    from graphviz import Digraph

    if graph is None:
        graph = Digraph()
    if node_id is None:
        node_id = itertools.count()   # fresh counter per top-level call (was a shared mutable default)
    label = parser.ruleNames[tree.getRuleIndex()] if hasattr(tree, 'getRuleIndex') else str(tree)
    my_id = str(next(node_id))
    graph.node(my_id, label)
    if parent is not None:
        graph.edge(parent, my_id)
    for i in range(tree.getChildCount()):
        child = tree.getChild(i)
        ast_to_graphviz(child, parser, graph, my_id, node_id)
    return graph

def display_soll_tree_graph(text):
    from IPython.display import display

    tree, parser = get_soll_tree(text)
    graph = ast_to_graphviz(tree, parser)
    display(graph)