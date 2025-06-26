# -*- coding: utf-8 -*-

import antlr4
from antlr4 import *
from graphviz import Digraph
from IPython.display import display
from pytamil.தமிழ் import எழுத்து as எழுத்து
from pytamil.தமிழ்.codegen.சொல்Lexer import சொல்Lexer
from pytamil.தமிழ்.codegen.சொல்Parser import சொல்Parser

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
    print (f"விரிதொடர்: {விரிதொடர்}")
    input_stream = antlr4.InputStream(விரிதொடர்)
    lexer = சொல்Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = சொல்Parser(stream)
    tree = parser.சொல்()
    return tree, parser

def print_soll_tree(text):
    tree, parser = get_soll_tree(text)
    print(tree.toStringTree(recog=parser))

def ast_to_graphviz(tree, parser, graph=None, parent=None, node_id=[0]):
    if graph is None:
        graph = Digraph()
    label = parser.ruleNames[tree.getRuleIndex()] if hasattr(tree, 'getRuleIndex') else str(tree)
    my_id = str(node_id[0])
    graph.node(my_id, label)
    if parent is not None:
        graph.edge(parent, my_id)
    node_id[0] += 1
    for i in range(tree.getChildCount()):
        child = tree.getChild(i)
        ast_to_graphviz(child, parser, graph, my_id, node_id)
    return graph

def display_soll_tree_graph(text):
    tree, parser = get_soll_tree(text)
    graph = ast_to_graphviz(tree, parser)
    display(graph)