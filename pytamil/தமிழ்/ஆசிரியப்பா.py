# -*- coding: utf-8 -*-

import sys
import antlr4
from antlr4 import *
from antlr4.tree.Trees import Trees
import os

# from codegen import codegen
from codegen.வெண்பாLexer import வெண்பாLexer
from codegen.வெண்பாParser import வெண்பாParser
from codecs import open
from nltk import Tree as nltkTree
from nltk.draw.tree import TreeView
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget
from nltk.treeprettyprinter import TreePrettyPrinter

import svgling


 
def main():
    infilename = os.path.join(os.path.dirname(__file__),'debug/வெண்பா-input.txt')
    outfilename = os.path.join(os.path.dirname(__file__),'debug/வெண்பா-output')
    data = open(infilename).read()   
    input_stream = antlr4.InputStream(data)
    lexer = வெண்பாLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = வெண்பாParser(stream)
    tree = parser.வெண்பா()
    saveas_txttree(tree,parser,outfilename)
    #saveas_pngtree(tree,parser,outfilename)


def saveas_txttree(tree, parser, outfilename):
     # print(tree.toStringTree())
    strtree = Trees.toStringTree(tree, None, parser)
    print(strtree)
    t = nltkTree.fromstring(strtree)
    # t.pretty_print(unicodelines=True)
    a = TreePrettyPrinter(t).text()
    print (a)
    # t.pprint(margin=70, indent=0, nodesep=u'', parens=u'()', quotes=False)
    # pprint(Trees.toStringTree(tree, None, parser), width=20, indent=4)
 
    with open(outfilename + ".txt", 'w', encoding='utf8') as f:
        f.write( a)

def saveas_pngtree(tree, parser, outfilename):
    # print(tree.toStringTree())
    strtree = Trees.toStringTree(tree, None, parser)
    print(strtree)
    # t = nltkTree.fromstring(strtree)
    # t = nltkTree.fromstring('(S (NP this tree) (VP (V is) (AdjP தமிழ்)))')
    # TreeView(t)._cframe.print_to_file(outfilename + '.ps')

    # cf = CanvasFrame()
    # t = nltkTree.fromstring('(S (NP this tree) (VP (V is) (AdjP தமிழ்)))')
    # tc = TreeWidget(cf.canvas(),t)
    # cf.add_widget(tc,10,10) # (10,10) offsets
    # cf.print_to_file(outfilename + '.ps')
    # cf.destroy()
    
    tlayout = svgling.draw_tree(("S", ("NP", ("D", "the"), ("N", "elephant")), ("VP", ("V", "saw"), ("NP", ("D", "the"), ("N", "rhinoceros")))))
    b = tlayout.get_svg()
    print(b)

if __name__ == '__main__':
    main()
