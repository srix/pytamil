# -*- coding: utf-8 -*-
"""
சொல் — ஒரு சொல் தமிழ் ஒலியமைப்புக்கு (phonotactics) உட்பட்டதா என ஆயும் கூறு.

    tree, parser = get_soll_tree('அம்மா')
    parser.getNumberOfSyntaxErrors()   # 0 எனில் இலக்கணம் ஏற்கிறது

விதிகள் resources/சொல்.g4-இல்: மொழிமுதல்/மொழியிடை/மொழியிறுதி எழுத்துக்கள், மெய்ம்மயக்கம்.
இலக்கணத்தில் இன்னும் இடைவெளிகள் உள்ளன (test_சொல்.py-இன் xfail காண்க).
"""
import itertools

from pytamil.தமிழ் import எழுத்து
from pytamil.தமிழ் import பாகுபடுத்தி
from pytamil.தமிழ்.codegen.சொல்Lexer import சொல்Lexer
from pytamil.தமிழ்.codegen.சொல்Parser import சொல்Parser

வேற்றுமை_உருபுகள் = ['ஐ', 'ஆல்', 'கு', 'இன்', 'அது', 'கண்']
நிறம் = []
மாதம் = []
பின்னம் = []
திசை = []


def get_soll_tree(text):
    """Expand the word and parse it with the சொல் grammar; returns (tree, parser)."""
    விரிதொடர் = எழுத்து.உயிர்மெய்விரி(text)
    பா = பாகுபடுத்தி.மரம்_கொடு(சொல்Lexer, சொல்Parser, 'சொல்', விரிதொடர்)
    return பா.மரம், பா.parser

def print_soll_tree(text):
    """Print the parse tree of a word in one-line LISP form."""
    tree, parser = get_soll_tree(text)
    print(tree.toStringTree(recog=parser))

def ast_to_graphviz(tree, parser, graph=None, parent=None, node_id=None):
    """Turn a parse tree into a graphviz Digraph (needs graphviz)."""
    # graphviz is optional; import here so that plain parsing works without it.
    from graphviz import Digraph   # pylint: disable=import-outside-toplevel

    if graph is None:
        graph = Digraph()
    if node_id is None:
        # fresh counter per top-level call (was a shared mutable default)
        node_id = itertools.count()
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
    """Display a word's parse tree in a notebook (needs graphviz and IPython)."""
    from IPython.display import display   # pylint: disable=import-outside-toplevel

    tree, parser = get_soll_tree(text)
    graph = ast_to_graphviz(tree, parser)
    display(graph)
