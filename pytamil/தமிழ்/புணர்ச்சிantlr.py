import antlr4
from antlr4 import *
from antlr4.tree.Trees import Trees
from antlr4.error.ErrorListener import ErrorListener

from pytamil.தமிழ் import எழுத்து as எழுத்து
from pytamil.தமிழ்.codegen.புணர்ச்சிவிதிகள்Lexer import புணர்ச்சிவிதிகள்Lexer
from pytamil.தமிழ்.codegen.புணர்ச்சிவிதிகள்Parser import புணர்ச்சிவிதிகள்Parser
from pytamil.தமிழ்.codegen.புணர்ச்சிவிதிகள்Listener import புணர்ச்சிவிதிகள்Listener
from pytamil.தமிழ் import பாகுபடுத்தி


class நம்புணர்ச்சிவிதிகள்Listener(புணர்ச்சிவிதிகள்Listener):
    
    # Enter a parse tree produced by புணர்ச்சிவிதிகள்Parser#நிலைமொழி_மாற்றம்.
    def enterநிலைமொழி_மாற்றம்(self, ctx:புணர்ச்சிவிதிகள்Parser.நிலைமொழி_மாற்றம்Context):
        pass

    # Enter a parse tree produced by புணர்ச்சிவிதிகள்Parser#வருமொழி_மாற்றம்.
    def enterவருமொழி_மாற்றம்(self, ctx:புணர்ச்சிவிதிகள்Parser.வருமொழி_மாற்றம்Context):
        pass

def தொடர்மொழி_ஆக்கு(விதி):
    தொமொ = விதி 
    # தொமொ = எழுத்து.உயிர்மெய்விரி(தொடர்)
    # தொமொ =  தொமொ.replace('நிலைமொழி',நிலைமொழி)
    # தொமொ = தொமொ.replace('வருமொழி',வருமொழி)

    பா = பாகுபடுத்தி.மரம்_கொடு(புணர்ச்சிவிதிகள்Lexer, புணர்ச்சிவிதிகள்Parser, 'புணர்ச்சிவிதிகள்', தொமொ)
    tree = பா.மரம்

    நம்listener = நம்புணர்ச்சிவிதிகள்Listener()
    walker = ParseTreeWalker()
    walker.walk(நம்listener, tree)
