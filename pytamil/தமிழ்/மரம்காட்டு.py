# -*- coding: utf-8 -*-
"""
மரம்காட்டு — ANTLR பாகுபாட்டு மரத்தை உரையாகக் காட்ட / சேமிக்க உதவும் கூறு.
nltk இங்குதான் தேவை; பகுப்பாய்வுக் கூறுகள் (வெண்பா, மாத்திரை ...) இதைச் சாரா.
"""
from antlr4.tree.Trees import Trees


def உரைமரம்(மரம், parser) -> str:
    """பாகுபாட்டு மரத்தை nltk-இன் TreePrettyPrinter வழி வரைந்த உரை."""
    from nltk import Tree as nltkTree
    try:
        from nltk.tree import TreePrettyPrinter
    except ImportError:  # nltk < 3.8
        from nltk.treeprettyprinter import TreePrettyPrinter

    return TreePrettyPrinter(nltkTree.fromstring(Trees.toStringTree(மரம், None, parser))).text()


def உரைமரம்_சேமி(மரம், parser, கோப்பு: str) -> str:
    """உரைமரத்தை கோப்பில் எழுதி, அந்த உரையையே திருப்பித் தரும்."""
    உரை = உரைமரம்(மரம், parser)
    with open(கோப்பு, 'w', encoding='utf8') as f:
        f.write(உரை)
    return உரை
