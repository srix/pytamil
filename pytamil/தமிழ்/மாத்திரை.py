# -*- coding: utf-8 -*-
"""
மாத்திரை — ஒரு பதத்தின் ஒவ்வோர் எழுத்துக்கும் அதன் வகையையும் மாத்திரை அளவையும் தரும் கூறு.

    வரிசை = மாத்திரைவரிசை_கொடு('ஊக்கம்')   # ஒவ்வோர் எழுத்துக்கும் ஒரு விவரம்()
    format(வரிசை)                          # 'ஊ:உயிர்நெடில்:2 க்:மெய்:0.5 ...'
    மொத்தமாத்திரை('ஊக்கம்')                # 4.0

எழுத்து வகைப்பாடு resources/மாத்திரை.g4 இலக்கணத்தால்; ஒவ்வொரு வகையின் மாத்திரை அளவு
resources/மாத்திரை.yaml-இல் (மாத்திரை_பட்டியல்). குறுக்கங்கள் (ஐகாரம், ஔகாரம், மகரம், ஆய்தம்,
குற்றியலுகரம், குற்றியலிகரம்) தனி விதிகளாக இலக்கணத்தில் உள்ளன.
"""
import os

import regex
import yaml
from yaml import Loader

from antlr4 import ParseTreeWalker

from pytamil.தமிழ் import எழுத்து
from pytamil.தமிழ் import parsehelper
from pytamil.தமிழ் import treetext
from pytamil.தமிழ் import விதிக்கோப்பு
from pytamil.தமிழ்.codegen.மாத்திரைLexer import மாத்திரைLexer
from pytamil.தமிழ்.codegen.மாத்திரைParser import மாத்திரைParser
from pytamil.தமிழ்.codegen.மாத்திரைListener import மாத்திரைListener


CURRDIR = os.path.dirname(os.path.realpath(__file__))


class சான்று:
    """A சான்று from மாத்திரை.yaml: 'பதம் = expected மாத்திரைவரிசை'."""

    def __init__(self, txt):
        val = regex.findall(r'(.+?)(?:>.*)*\=(.*)', txt)
        self.பதம் = val[0][0].strip()
        self.மாத்திரைவரிசை = val[0][1].strip()


class விவரம்:
    """ஓர் எழுத்தின் மாத்திரை விவரம்: எழுத்து, அதன் வகை, மாத்திரை அளவு."""

    def __init__(self, எழுத்து_, மாத்திரைவகை, மாத்திரைஎண், புணர்மொழி=False):
        self.எழுத்து = எழுத்து_
        self.மாத்திரைவகை = மாத்திரைவகை
        self.மாத்திரைஎண் = மாத்திரைஎண்
        self.புணர்மொழி = புணர்மொழி


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
    """Walks the parse tree, appending one விவரம்() per எழுத்து to `seq`."""

    def __init__(self, பட்டியல்):
        self.seq = []
        self.மாத்திரை_பட்டியல் = பட்டியல்

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
        self.seq.append(விவரம்('ஃ', 'ஆய்தக்குறுக்கம்', self.மாத்திரை_பட்டியல்['ஆய்தக்குறுக்கம்']))

        எழுத்துவரிசை = எழுத்து.எழுத்தாக்கு(ctx.getText())
        எழுத்துவரிசை = எழுத்துவரிசை[1:]
        உயிர்மெய் = எழுத்து.உயிர்மெய்சேர்(எழுத்துவரிசை)

        if உயிர்மெய் == 'றி':
            self.seq.append(விவரம்('றி', 'உயிர்மெய்க்குறில்',
                                   self.மாத்திரை_பட்டியல்['உயிர்மெய்க்குறில்']))

        elif உயிர்மெய் == 'டீ':
            self.seq.append(விவரம்('டீ', 'உயிர்மெய்நெடில்',
                                   self.மாத்திரை_பட்டியல்['உயிர்மெய்நெடில்']))

    def enterமகரக்குறுக்கம்_தனிமொழி(self, ctx:மாத்திரைParser.மகரக்குறுக்கம்_தனிமொழிContext):
        எழுத்துவரிசை = எழுத்து.எழுத்தாக்கு(ctx.getText())
        எழுத்துவரிசை = எழுத்துவரிசை[:-1]
        உயிர்மெய் = எழுத்து.உயிர்மெய்சேர்(எழுத்துவரிசை)

        self.seq.append(விவரம்(உயிர்மெய், 'மெய்', self.மாத்திரை_பட்டியல்['மெய்']))
        self.seq.append(விவரம்('ம்', 'மகரக்குறுக்கம்', self.மாத்திரை_பட்டியல்['மகரக்குறுக்கம்']))

    def enterமகரக்குறுக்கம்_புணர்மொழி(self, ctx:மாத்திரைParser.மகரக்குறுக்கம்_புணர்மொழிContext):
        எழுத்துவரிசை = எழுத்து.எழுத்தாக்கு(ctx.getText())
        எழுத்துவரிசை = எழுத்துவரிசை[1:]
        உயிர்மெய் = எழுத்து.உயிர்மெய்சேர்(எழுத்துவரிசை)

        self.seq.append(விவரம்('ம்', 'மகரக்குறுக்கம்', self.மாத்திரை_பட்டியல்['மகரக்குறுக்கம்'],
                               புணர்மொழி=True))
        self.seq.append(விவரம்(உயிர்மெய், 'உயிர்மெய்க்குறில்',
                               self.மாத்திரை_பட்டியல்['உயிர்மெய்க்குறில்']))

    def enterகுற்றியலிகரம்_தனிமொழி(self, ctx:மாத்திரைParser.குற்றியலிகரம்_தனிமொழிContext):
        எழுத்துவரிசை = எழுத்து.எழுத்தாக்கு(ctx.getText())
        குற்றியலிகரம் = எழுத்து.உயிர்மெய்சேர்(எழுத்துவரிசை[:-2])
        யா = எழுத்து.உயிர்மெய்சேர்(எழுத்துவரிசை[-2:])

        self.seq.append(விவரம்(குற்றியலிகரம், 'குற்றியலிகரம்',
                               self.மாத்திரை_பட்டியல்['குற்றியலிகரம்']))
        self.seq.append(விவரம்(யா, 'உயிர்மெய்நெடில்',
                               self.மாத்திரை_பட்டியல்['உயிர்மெய்நெடில்']))

    def enterகுற்றியலிகரம்_புணர்மொழி(self, ctx:மாத்திரைParser.குற்றியலிகரம்_புணர்மொழிContext):
        எழுத்துவரிசை = எழுத்து.எழுத்தாக்கு(ctx.getText())
        குற்றியலிகரம்_எழுத்துவரிசை = எழுத்துவரிசை[:2]
        உயிர்மெய் = எழுத்து.உயிர்மெய்சேர்(குற்றியலிகரம்_எழுத்துவரிசை)

        self.seq.append(விவரம்(உயிர்மெய், 'குற்றியலிகரம்',
                               self.மாத்திரை_பட்டியல்['குற்றியலிகரம்'], புணர்மொழி=True))

        ய_எழுத்துவரிசை = எழுத்துவரிசை[2:]
        உயிர்மெய் = எழுத்து.உயிர்மெய்சேர்(ய_எழுத்துவரிசை)
        if ய_எழுத்துவரிசை[1] in எழுத்து.உயிர்க்குறில்:
            எழுத்துவகை = 'உயிர்மெய்க்குறில்'
        else:
            எழுத்துவகை = 'உயிர்மெய்நெடில்'
        self.seq.append(விவரம்(உயிர்மெய், எழுத்துவகை, self.மாத்திரை_பட்டியல்[எழுத்துவகை]))

    def மாத்திரை_கனக்கு(self, ctx):
        """Append a விவரம் for an எழுத்து node sitting directly under the மாத்திரை rule."""
        if ctx.parentCtx.parentCtx.parentCtx.getRuleIndex() == ctx.parser.RULE_மாத்திரை:
            எழுத்துவரிசை = எழுத்து.எழுத்தாக்கு(ctx.getText())
            உயிர்மெய் = எழுத்து.உயிர்மெய்சேர்(எழுத்துவரிசை)
            எழுத்துவகை = ctx.parser.ruleNames[ctx.getRuleIndex()]
            மாத்திரை_எண் = self.மாத்திரை_பட்டியல்[எழுத்துவகை]
            self.seq.append(விவரம்(உயிர்மெய், எழுத்துவகை, மாத்திரை_எண்))


def printtree(தொடர்):
    """Return the parse tree of a word as drawn text (needs nltk)."""
    tree, parser = gettree(தொடர்)
    return treetext.as_text(tree, parser)

def printtree_tofile(தொடர், outfilename):
    """Write what printtree() returns to a file."""
    tree, parser = gettree(தொடர்)
    treetext.save_text(tree, parser, outfilename)

def gettree(தொடர்):
    """Parse a word (in normal orthography) with the மாத்திரை grammar; returns (tree, parser)."""
    விரிதொடர் = எழுத்து.உயிர்மெய்விரி(தொடர்)
    result = parsehelper.parse(மாத்திரைLexer, மாத்திரைParser, 'மாத்திரை', விரிதொடர்)
    return result.tree, result.parser

def மாத்திரைவரிசை_கொடு(தொடர்):
    """One விவரம்() per எழுத்து of the word, in order."""
    tree, _ = gettree(தொடர்)

    நம்listener = நம்மாத்திரைListener(மாத்திரை_பட்டியல்)
    walker = ParseTreeWalker()
    walker.walk(நம்listener, tree)

    return நம்listener.seq

def மொத்தமாத்திரை(தொடர்):
    """Total மாத்திரை of a word: sum of the per-letter values from மாத்திரைவரிசை_கொடு."""
    return sum(விவரம்.மாத்திரைஎண் for விவரம் in மாத்திரைவரிசை_கொடு(தொடர்))

def getசான்றுகள்(entries, சான்றுகள்):
    """Build a சான்று from every சான்று in the YAML; appends to and returns `சான்றுகள்`."""
    வரிகள் = விதிக்கோப்பு.items(entries, "சான்று")
    சான்றுகள்.extend(சான்று(txt) for texts in வரிகள் for txt in texts)
    return சான்றுகள்

# Shadows the `format` builtin, but மாத்திரை.format() is the existing public interface;
# renaming it would break callers.
def format(மாத்திரைவரிசை):   # pylint: disable=redefined-builtin
    """Render a மாத்திரைவரிசை as 'எழுத்து:வகை:எண்' text."""
    textstr = ''
    for மாத்திரைவிவரம் in மாத்திரைவரிசை:
        textstr = (textstr + மாத்திரைவிவரம்.எழுத்து + ':' + மாத்திரைவிவரம்.மாத்திரைவகை
                   + ':' + str(மாத்திரைவிவரம்.மாத்திரைஎண்) + ' ')

    return textstr

def formatsimple(மாத்திரைவரிசை):
    """Render a மாத்திரைவரிசை as 'எழுத்து:வகை' text, without the மாத்திரை value."""
    textstr = ""
    for மாத்திரைவிவரம் in மாத்திரைவரிசை:
        textstr = textstr + மாத்திரைவிவரம்.எழுத்து + ':' + மாத்திரைவிவரம்.மாத்திரைவகை + ' '

    return textstr

def load(filename):
    """Load the first document of மாத்திரை.yaml, which holds மாத்திரை_பட்டியல்."""
    with open(filename, "r", encoding='utf8') as fo:
        docs = list(yaml.load_all(fo, Loader=Loader))
    return docs[0]

மாத்திரைகள் = load(os.path.join(CURRDIR, "resources/மாத்திரை.yaml"))
மாத்திரை_பட்டியல் = மாத்திரைகள்["மாத்திரை_பட்டியல்"]
