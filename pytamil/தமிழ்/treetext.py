# -*- coding: utf-8 -*-
"""
treetext — draw an ANTLR parse tree as text, and save it.

nltk is needed only here; the analysis modules (வெண்பா, மாத்திரை ...) do not depend on it.
"""
from antlr4.tree.Trees import Trees


def as_text(tree, parser) -> str:
    """The parse tree drawn as text by nltk's TreePrettyPrinter."""
    # nltk is optional; importing it here keeps the analysis modules independent of it.
    # pylint: disable=import-outside-toplevel
    from nltk import Tree as nltkTree
    try:
        from nltk.tree import TreePrettyPrinter
    except ImportError:  # nltk < 3.8
        from nltk.treeprettyprinter import TreePrettyPrinter

    return TreePrettyPrinter(nltkTree.fromstring(Trees.toStringTree(tree, None, parser))).text()


def save_text(tree, parser, path: str) -> str:
    """Write the drawn tree to `path` and return that same text."""
    text = as_text(tree, parser)
    with open(path, 'w', encoding='utf8') as f:
        f.write(text)
    return text
