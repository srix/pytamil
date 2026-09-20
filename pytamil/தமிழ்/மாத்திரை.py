# -*- coding: utf-8 -*-
from codecs import open
import os
import sys

import regex
import yaml
from tamil import utf8 as tamilutf8
from yaml import Loader, Dumper

import antlr4
from antlr4 import *
from antlr4.tree.Trees import Trees

from pytamil.தமிழ் import எழுத்து as எழுத்து
# from codegen import codegen
from pytamil.தமிழ்.codegen.மாத்திரைLexer import மாத்திரைLexer
from pytamil.தமிழ்.codegen.மாத்திரைParser import மாத்திரைParser
from pytamil.தமிழ்.codegen.மாத்திரைListener import மாத்திரைListener
from pytamil.தமிழ் import பாகுபடுத்தி
# from pytamil.தமிழ்.codegen.மாத்திரைVisitor import மாத்திரைVisitor


CURRDIR = os.path.dirname(os.path.realpath(__file__))





class சான்று:
     def __init__(self, txt):
        val = regex.findall(r'(.+?)(?:>.*)*\=(.*)',txt)
        self.பதம் = val[0][0].strip()
        self.மாத்திரைவரிசை = val[0][1].strip()
      
# pylint: disable=invalid-name
class விவரம்:
    def __init__(self, எழுத்து, மாத்திரைவகை, மாத்திரைஎண், புணர்மொழி=False):
        self.எழுத்து = எழுத்து
        self.மாத்திரைவகை = மாத்திரைவகை
        self.மாத்திரைஎண் = மாத்திரைஎண்
        self.புணர்மொழி=புணர்மொழி
        


#                      மாத்திரை                                           
#       __________________|_________________________________________       
#      |         |                   மொழியிடை                    |     
#      |         |                      |                           |      
#  மொழிமுதல்  மொழியிடை          உயிர்மெய்க்குறில்               மொழியிறுதி
#      |         |         _____________|_______________            |      
# உயிர்நெடில்   மெய்     மெய்                     உயிர்க்குறில்    மெய்   
#      |         |        |                             |           |      
#      ஊ         க்       க்                            அ           ம்    

# calculate மாத்திரை for rules at second level. 

class நம்மாத்திரைListener(மாத்திரைListener):
    def __init__(self,மாத்திரைகள்):
        self.seq = []
        self.மாத்திரை_பட்டியல் = மாத்திரை_பட்டியல்

    def enterஉயிர்க்குறில்(self, ctx:மாத்திரைParser.உயிர்க்குறில்Context):
        self.மாத்திரை_கனக்கு(ctx)
    
    def enterஉயிர்நெடில்(self, ctx:மாத்திரைParser.உயிர்நெடில்Context):
        self.மாத்திரை_கனக்கு(ctx)

    def enterமெய்(self, ctx:மாத்திரைParser.மெய்Context):
        self.மாத்திரை_கனக்கு(ctx)

    def enterஆய்தம்(self, ctx:மாத்திரைParser.ஆய்தம்Context):
        self.மாத்திரை_கனக்கு(ctx)

    def enterஉயிர்மெய்க்குறில்(self, ctx:மாத்திரைParser.உயிர்மெய்க்குறில்Context):
        self.மாத்திரை_கனக்கு(ctx)

    def enterஉயிர்மெய்நெடில்(self, ctx:மாத்திரைParser.உயிர்மெய்நெடில்Context):
        self.மாத்திரை_கனக்கு(ctx)

    def enterஉயிரளபெடை(self, ctx:மாத்திரைParser.உயிரளபெடைContext):
        self.மாத்திரை_கனக்கு(ctx)

    def enterஒற்றளபெடை(self, ctx:மாத்திரைParser.ஒற்றளபெடைContext):
        self.மாத்திரை_கனக்கு(ctx)

    def enterஔகாரக்குறுக்கம்(self, ctx:மாத்திரைParser.ஔகாரக்குறுக்கம்Context):
        self.மாத்திரை_கனக்கு(ctx)

    def enterகுற்றியலுகரம்(self, ctx:மாத்திரைParser.குற்றியலுகரம்Context):
        self.மாத்திரை_கனக்கு(ctx)

    def enterஐகாரக்குறுக்கம்_முதல்(self, ctx:மாத்திரைParser.ஐகாரக்குறுக்கம்_முதல்Context):
        self.மாத்திரை_கனக்கு(ctx)

    def enterஐகாரக்குறுக்கம்_இடைகடை(self, ctx:மாத்திரைParser.ஐகாரக்குறுக்கம்_இடைகடைContext):
        self.மாத்திரை_கனக்கு(ctx)

    def enterஆய்தக்குறுக்கம்(self, ctx:மாத்திரைParser.ஆய்தக்குறுக்கம்Context):
        self.seq.append( விவரம்('ஃ', 'ஆய்தக்குறுக்கம்' , மாத்திரை_பட்டியல்['ஆய்தக்குறுக்கம்'] )  )

        எழுத்துவரிசை = எழுத்து.எழுத்தாக்கு(ctx.getText())
        எழுத்துவரிசை = எழுத்துவரிசை[1:]
        உயிர்மெய் = எழுத்து.உயிர்மெய்சேர்(எழுத்துவரிசை)
        
        if உயிர்மெய் == 'றி':
            self.seq.append( விவரம்('றி', 'உயிர்மெய்க்குறில்' , மாத்திரை_பட்டியல்['உயிர்மெய்க்குறில்'])  )

        elif உயிர்மெய் == 'டீ':
            self.seq.append( விவரம்('டீ', 'உயிர்மெய்நெடில்' , மாத்திரை_பட்டியல்['உயிர்மெய்நெடில்'])  )

    def enterமகரக்குறுக்கம்_தனிமொழி(self, ctx:மாத்திரைParser.மகரக்குறுக்கம்_தனிமொழிContext):
        எழுத்துவரிசை = எழுத்து.எழுத்தாக்கு(ctx.getText())
        எழுத்துவரிசை = எழுத்துவரிசை[:-1]
        உயிர்மெய் = எழுத்து.உயிர்மெய்சேர்(எழுத்துவரிசை)
        
        self.seq.append(விவரம்(உயிர்மெய், 'மெய்' , மாத்திரை_பட்டியல்['மெய்']) )
        self.seq.append(விவரம்('ம்', 'மகரக்குறுக்கம்' , மாத்திரை_பட்டியல்['மகரக்குறுக்கம்']) )

    def enterமகரக்குறுக்கம்_புணர்மொழி(self, ctx:மாத்திரைParser.மகரக்குறுக்கம்_புணர்மொழிContext):
        எழுத்துவரிசை = எழுத்து.எழுத்தாக்கு(ctx.getText())
        எழுத்துவரிசை = எழுத்துவரிசை[1:]
        உயிர்மெய் = எழுத்து.உயிர்மெய்சேர்(எழுத்துவரிசை)

        self.seq.append(விவரம்('ம்', 'மகரக்குறுக்கம்' , மாத்திரை_பட்டியல்['மகரக்குறுக்கம்'], புணர்மொழி=True) )
        self.seq.append(விவரம்(உயிர்மெய், 'உயிர்மெய்க்குறில்' , மாத்திரை_பட்டியல்['உயிர்மெய்க்குறில்']) )

    def enterகுற்றியலிகரம்_தனிமொழி(self, ctx:மாத்திரைParser.குற்றியலிகரம்_தனிமொழிContext):
        எழுத்துவரிசை = எழுத்து.எழுத்தாக்கு(ctx.getText())
        எழுத்துவரிசை = எழுத்துவரிசை[1:]
        உயிர்மெய் = எழுத்து.உயிர்மெய்சேர்(எழுத்துவரிசை)

        self.seq.append(விவரம்('மி', 'குற்றியலிகரம்' , மாத்திரை_பட்டியல்['குற்றியலிகரம்']))
        self.seq.append(விவரம்('யா', 'உயிர்மெய்நெடில்' , மாத்திரை_பட்டியல்['உயிர்மெய்நெடில்']))

    def enterகுற்றியலிகரம்_புணர்மொழி(self, ctx:மாத்திரைParser.குற்றியலிகரம்_புணர்மொழிContext):
        எழுத்துவரிசை = எழுத்து.எழுத்தாக்கு(ctx.getText())
        குற்றியலிகரம்_எழுத்துவரிசை= எழுத்துவரிசை[:2]
        உயிர்மெய் = எழுத்து.உயிர்மெய்சேர்(குற்றியலிகரம்_எழுத்துவரிசை)

        self.seq.append(விவரம்(உயிர்மெய், 'குற்றியலிகரம்' , மாத்திரை_பட்டியல்['குற்றியலிகரம்'], புணர்மொழி=True))

        ய_எழுத்துவரிசை = எழுத்துவரிசை[2:]
        உயிர்மெய் = எழுத்து.உயிர்மெய்சேர்(ய_எழுத்துவரிசை)
        எழுத்துவகை = None
        if ய_எழுத்துவரிசை[1] in எழுத்து.உயிர்க்குறில்:
            எழுத்துவகை =  'உயிர்மெய்க்குறில்'
        else:
            எழுத்துவகை =  'உயிர்மெய்நெடில்'
        self.seq.append(விவரம்(உயிர்மெய், எழுத்துவகை , மாத்திரை_பட்டியல்[எழுத்துவகை]))


    def மாத்திரை_கனக்கு(self, ctx):
        if ctx.parentCtx.parentCtx.parentCtx.getRuleIndex() == ctx.parser.RULE_மாத்திரை:
            எழுத்துவரிசை = எழுத்து.எழுத்தாக்கு(ctx.getText())
            உயிர்மெய் = எழுத்து.உயிர்மெய்சேர்(எழுத்துவரிசை)
            எழுத்துவகை =  ctx.parser.ruleNames[ctx.getRuleIndex()]
            மாத்திரை_எண் = மாத்திரை_பட்டியல்[எழுத்துவகை]
            self.seq.append(விவரம்(உயிர்மெய், எழுத்துவகை , மாத்திரை_எண்))


# class நம்மாத்திரைVisitor(மாத்திரைVisitor):
#     def __init__(self):
#         self.seq = []

#     def visitமொழியிடை(self, ctx:மாத்திரைParser.மொழியிடைContext):
#         self.seq.append([ctx.getText(), 1])
#         return self.visitChildren(ctx)
 

def printtree(தொடர்):
    from nltk import Tree as nltkTree
    try:
        from nltk.tree import TreePrettyPrinter
    except ImportError:  # nltk < 3.8
        from nltk.treeprettyprinter import TreePrettyPrinter

    tree, parser = gettree(தொடர்)
    strtree = Trees.toStringTree(tree, None, parser)
    t = nltkTree.fromstring(strtree)
    # t.pretty_print()
    treestr = TreePrettyPrinter(t).text()
    # print (treestr)
    # t.pprint(margin=70, indent=0, nodesep=u'', parens=u'()', quotes=False)
    # pprint(Trees.toStringTree(tree, None, parser), width=20, indent=4)
 
    return treestr

def printtree_tofile(தொடர், outfilename):
    treestr = printtree(தொடர்)
    with open(outfilename, 'w', encoding='utf8') as f:
        f.write( treestr)

def gettree(தொடர்):
    """Parse a word (in normal orthography) with the மாத்திரை grammar; returns (tree, parser)."""
    விரிதொடர் = எழுத்து.உயிர்மெய்விரி(தொடர்)
    பா = பாகுபடுத்தி.மரம்_கொடு(மாத்திரைLexer, மாத்திரைParser, 'மாத்திரை', விரிதொடர்)
    return பா.மரம், பா.parser

def மாத்திரைவரிசை_கொடு(தொடர்):
    tree, parser = gettree(தொடர்)

    நம்listener = நம்மாத்திரைListener(மாத்திரை_பட்டியல்)
    walker = ParseTreeWalker()
    walker.walk(நம்listener, tree)

    # நம்visitor = நம்மாத்திரைVisitor()
    # நம்visitor.visit(tree)

    return நம்listener.seq

def மொத்தமாத்திரை(தொடர்):
    """Total மாத்திரை of a word: sum of the per-letter values from மாத்திரைவரிசை_கொடு."""
    return sum(விவரம்.மாத்திரைஎண் for விவரம் in மாத்திரைவரிசை_கொடு(தொடர்))

def getசான்றுகள்(entries,சான்றுகள்):
    for key in entries:
        value = entries[key]
        if type(value) is dict:
            சான்றுகள் = getசான்றுகள்(value,சான்றுகள்)
        elif type(value) is list:
            for item in value:
                if "சான்று" in item.keys():
                    for txt in  item["சான்று"]:
                        சா = சான்று(txt)
                        சான்றுகள்.append(சா)

    return சான்றுகள்

def format(மாத்திரைவரிசை):
    textstr=''
    for மாத்திரைவிவரம் in மாத்திரைவரிசை:
        textstr = textstr + மாத்திரைவிவரம்.எழுத்து + ':' + மாத்திரைவிவரம்.மாத்திரைவகை + ':' + str(மாத்திரைவிவரம்.மாத்திரைஎண்) + ' '

    return textstr

def formatsimple(மாத்திரைவரிசை):
    textstr=""
    for மாத்திரைவிவரம் in மாத்திரைவரிசை:
        # textstr= textstr +எ[0] + ':' + எ[1] + ' '
        textstr = textstr + மாத்திரைவிவரம்.எழுத்து + ':' + மாத்திரைவிவரம்.மாத்திரைவகை +  ' '

    return textstr

def load(filename):
    fo = open(filename, "r")
    மாத்திரை_yaml = yaml.load_all(fo,Loader=Loader)
    docs = list(மாத்திரை_yaml)
    entries = docs[0]

    entries2 = docs[1]
    சான்றுகள் = []
    சான்றுகள் = getசான்றுகள்(entries2,சான்றுகள் )

    return entries

மாத்திரைகள் = {}
மாத்திரைகள் = load(os.path.join(CURRDIR,"resources/மாத்திரை.yaml"))
மாத்திரை_பட்டியல் = மாத்திரைகள்["மாத்திரை_பட்டியல்"]
