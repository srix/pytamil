# -*- coding: utf-8 -*-
"""
புணர்ச்சிantlr — புணர்ச்சி விதிகளை ANTLR வழி பாகுபடுத்தும் முயற்சி (முழுமையடையாதது).

தற்போது புணர்ச்சி.py TatSu (resources/புணர்ச்சிவிதிகள்.ebnf) வழியே வேலை செய்கிறது; இது அதே
விதிகளை resources/புணர்ச்சிவிதிகள்.g4 வழி பாகுபடுத்தும் மாற்றுப் பாதை. listener இன்னும்
எதையும் செய்வதில்லை — TatSu → ANTLR மாற்றம் நிறைவுறும்போது இதுவே முதன்மையாகும்.
"""
from antlr4 import ParseTreeWalker

from pytamil.தமிழ் import parsehelper
from pytamil.தமிழ்.codegen.புணர்ச்சிவிதிகள்Lexer import புணர்ச்சிவிதிகள்Lexer
from pytamil.தமிழ்.codegen.புணர்ச்சிவிதிகள்Parser import புணர்ச்சிவிதிகள்Parser
from pytamil.தமிழ்.codegen.புணர்ச்சிவிதிகள்Listener import புணர்ச்சிவிதிகள்Listener


class நம்புணர்ச்சிவிதிகள்Listener(புணர்ச்சிவிதிகள்Listener):
    """Listener meant to collect நிலைமொழி/வருமொழி changes; not filled in yet."""

    # Enter a parse tree produced by புணர்ச்சிவிதிகள்Parser#நிலைமொழி_மாற்றம்.
    def enterநிலைமொழி_மாற்றம்(self, ctx:புணர்ச்சிவிதிகள்Parser.நிலைமொழி_மாற்றம்Context):
        pass

    # Enter a parse tree produced by புணர்ச்சிவிதிகள்Parser#வருமொழி_மாற்றம்.
    def enterவருமொழி_மாற்றம்(self, ctx:புணர்ச்சிவிதிகள்Parser.வருமொழி_மாற்றம்Context):
        pass


def தொடர்மொழி_ஆக்கு(விதி):
    """Parse one புணர்ச்சி விதி with ANTLR and walk it with the listener."""
    result = parsehelper.parse(புணர்ச்சிவிதிகள்Lexer, புணர்ச்சிவிதிகள்Parser,
                               'புணர்ச்சிவிதிகள்', விதி)

    நம்listener = நம்புணர்ச்சிவிதிகள்Listener()
    walker = ParseTreeWalker()
    walker.walk(நம்listener, result.tree)
