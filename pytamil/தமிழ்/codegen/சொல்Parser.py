# Generated from சொல்.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,58,223,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        1,0,1,0,3,0,83,8,0,1,1,1,1,5,1,87,8,1,10,1,12,1,90,9,1,1,1,1,1,1,
        2,1,2,1,3,1,3,3,3,98,8,3,1,4,1,4,1,4,1,4,1,4,3,4,105,8,4,1,4,1,4,
        1,4,3,4,110,8,4,1,5,1,5,1,5,1,5,3,5,116,8,5,1,6,1,6,1,6,3,6,121,
        8,6,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,11,1,12,
        1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,3,14,156,8,14,1,15,1,15,1,15,1,16,
        1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,19,1,19,1,19,1,20,1,20,
        1,20,1,21,1,21,1,21,1,22,1,22,1,22,1,23,1,23,1,23,1,24,1,24,1,24,
        1,25,1,25,1,25,1,26,1,26,1,26,1,27,1,27,1,27,1,28,1,28,1,28,1,29,
        1,29,1,30,1,30,1,30,1,31,1,31,1,32,1,32,1,33,1,33,1,34,1,34,1,35,
        1,35,1,36,1,36,1,37,1,37,1,38,1,38,1,39,1,39,1,39,1,88,0,40,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,0,25,1,0,1,7,2,0,5,
        5,7,10,1,0,11,12,1,0,13,14,2,0,11,11,14,16,3,0,11,11,15,15,18,21,
        3,0,11,12,14,15,23,26,2,0,3,3,17,17,3,0,1,1,3,3,6,6,6,0,1,1,3,3,
        6,8,17,17,22,22,27,27,2,0,4,4,17,17,3,0,1,1,3,8,22,22,5,0,1,1,3,
        3,6,6,17,17,22,22,6,0,1,1,3,3,6,8,17,17,22,22,32,32,1,0,33,49,3,
        0,17,17,28,28,30,30,2,0,33,36,39,42,4,0,11,12,14,14,16,16,18,18,
        4,0,15,15,19,20,23,25,50,50,4,0,1,10,17,17,22,22,27,32,5,0,1,1,3,
        4,6,6,27,27,32,32,3,0,2,2,5,5,7,10,3,0,17,17,22,22,28,31,1,0,52,
        58,8,0,2,2,5,5,7,10,17,17,22,22,29,29,31,31,51,51,209,0,82,1,0,0,
        0,2,84,1,0,0,0,4,93,1,0,0,0,6,97,1,0,0,0,8,109,1,0,0,0,10,115,1,
        0,0,0,12,120,1,0,0,0,14,122,1,0,0,0,16,125,1,0,0,0,18,128,1,0,0,
        0,20,130,1,0,0,0,22,132,1,0,0,0,24,135,1,0,0,0,26,138,1,0,0,0,28,
        155,1,0,0,0,30,157,1,0,0,0,32,160,1,0,0,0,34,163,1,0,0,0,36,166,
        1,0,0,0,38,169,1,0,0,0,40,172,1,0,0,0,42,175,1,0,0,0,44,178,1,0,
        0,0,46,181,1,0,0,0,48,184,1,0,0,0,50,187,1,0,0,0,52,190,1,0,0,0,
        54,193,1,0,0,0,56,196,1,0,0,0,58,199,1,0,0,0,60,201,1,0,0,0,62,204,
        1,0,0,0,64,206,1,0,0,0,66,208,1,0,0,0,68,210,1,0,0,0,70,212,1,0,
        0,0,72,214,1,0,0,0,74,216,1,0,0,0,76,218,1,0,0,0,78,220,1,0,0,0,
        80,83,3,4,2,0,81,83,3,2,1,0,82,80,1,0,0,0,82,81,1,0,0,0,83,1,1,0,
        0,0,84,88,3,8,4,0,85,87,3,12,6,0,86,85,1,0,0,0,87,90,1,0,0,0,88,
        89,1,0,0,0,88,86,1,0,0,0,89,91,1,0,0,0,90,88,1,0,0,0,91,92,3,10,
        5,0,92,3,1,0,0,0,93,94,3,6,3,0,94,5,1,0,0,0,95,98,3,16,8,0,96,98,
        3,64,32,0,97,95,1,0,0,0,97,96,1,0,0,0,98,7,1,0,0,0,99,110,3,62,31,
        0,100,110,3,64,32,0,101,104,7,0,0,0,102,105,3,62,31,0,103,105,3,
        64,32,0,104,102,1,0,0,0,104,103,1,0,0,0,105,110,1,0,0,0,106,110,
        3,22,11,0,107,110,3,24,12,0,108,110,3,26,13,0,109,99,1,0,0,0,109,
        100,1,0,0,0,109,101,1,0,0,0,109,106,1,0,0,0,109,107,1,0,0,0,109,
        108,1,0,0,0,110,9,1,0,0,0,111,116,3,62,31,0,112,116,3,64,32,0,113,
        116,7,1,0,0,114,116,3,74,37,0,115,111,1,0,0,0,115,112,1,0,0,0,115,
        113,1,0,0,0,115,114,1,0,0,0,116,11,1,0,0,0,117,121,3,28,14,0,118,
        121,3,58,29,0,119,121,3,60,30,0,120,117,1,0,0,0,120,118,1,0,0,0,
        120,119,1,0,0,0,121,13,1,0,0,0,122,123,3,68,34,0,123,124,3,62,31,
        0,124,15,1,0,0,0,125,126,3,68,34,0,126,127,3,64,32,0,127,17,1,0,
        0,0,128,129,7,2,0,0,129,19,1,0,0,0,130,131,7,3,0,0,131,21,1,0,0,
        0,132,133,5,8,0,0,133,134,7,4,0,0,134,23,1,0,0,0,135,136,5,17,0,
        0,136,137,7,5,0,0,137,25,1,0,0,0,138,139,5,22,0,0,139,140,7,6,0,
        0,140,27,1,0,0,0,141,156,3,30,15,0,142,156,3,32,16,0,143,156,3,34,
        17,0,144,156,3,36,18,0,145,156,3,38,19,0,146,156,3,40,20,0,147,156,
        3,42,21,0,148,156,3,44,22,0,149,156,3,46,23,0,150,156,3,48,24,0,
        151,156,3,50,25,0,152,156,3,52,26,0,153,156,3,54,27,0,154,156,3,
        56,28,0,155,141,1,0,0,0,155,142,1,0,0,0,155,143,1,0,0,0,155,144,
        1,0,0,0,155,145,1,0,0,0,155,146,1,0,0,0,155,147,1,0,0,0,155,148,
        1,0,0,0,155,149,1,0,0,0,155,150,1,0,0,0,155,151,1,0,0,0,155,152,
        1,0,0,0,155,153,1,0,0,0,155,154,1,0,0,0,156,29,1,0,0,0,157,158,5,
        2,0,0,158,159,5,1,0,0,159,31,1,0,0,0,160,161,5,8,0,0,161,162,7,7,
        0,0,162,33,1,0,0,0,163,164,5,27,0,0,164,165,7,8,0,0,165,35,1,0,0,
        0,166,167,5,9,0,0,167,168,7,9,0,0,168,37,1,0,0,0,169,170,5,5,0,0,
        170,171,7,10,0,0,171,39,1,0,0,0,172,173,5,7,0,0,173,174,3,68,34,
        0,174,41,1,0,0,0,175,176,5,17,0,0,176,177,7,11,0,0,177,43,1,0,0,
        0,178,179,5,28,0,0,179,180,7,11,0,0,180,45,1,0,0,0,181,182,5,29,
        0,0,182,183,7,12,0,0,183,47,1,0,0,0,184,185,5,22,0,0,185,186,3,68,
        34,0,186,49,1,0,0,0,187,188,5,30,0,0,188,189,7,11,0,0,189,51,1,0,
        0,0,190,191,5,31,0,0,191,192,7,12,0,0,192,53,1,0,0,0,193,194,5,32,
        0,0,194,195,7,8,0,0,195,55,1,0,0,0,196,197,5,10,0,0,197,198,7,13,
        0,0,198,57,1,0,0,0,199,200,7,14,0,0,200,59,1,0,0,0,201,202,7,15,
        0,0,202,203,7,16,0,0,203,61,1,0,0,0,204,205,7,17,0,0,205,63,1,0,
        0,0,206,207,7,18,0,0,207,65,1,0,0,0,208,209,5,51,0,0,209,67,1,0,
        0,0,210,211,7,19,0,0,211,69,1,0,0,0,212,213,7,20,0,0,213,71,1,0,
        0,0,214,215,7,21,0,0,215,73,1,0,0,0,216,217,7,22,0,0,217,75,1,0,
        0,0,218,219,7,23,0,0,219,77,1,0,0,0,220,221,7,24,0,0,221,79,1,0,
        0,0,8,82,88,97,104,109,115,120,155
    ]

class சொல்Parser ( Parser ):

    grammarFileName = "சொல்.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\u0B95\\u0BCD'", "'\\u0B99\\u0BCD'", 
                     "'\\u0B9A\\u0BCD'", "'\\u0BA4\\u0BCD'", "'\\u0BA8\\u0BCD'", 
                     "'\\u0BAA\\u0BCD'", "'\\u0BAE\\u0BCD'", "'\\u0B9E\\u0BCD'", 
                     "'\\u0BA3\\u0BCD'", "'\\u0BA9\\u0BCD'", "'\\u0B85'", 
                     "'\\u0B87'", "'\\u0BAF\\u0BBE'", "'\\u0B8E'", "'\\u0B86'", 
                     "'\\u0B92'", "'\\u0BAF\\u0BCD'", "'\\u0B89'", "'\\u0B8A'", 
                     "'\\u0B93'", "'\\u0B93\\u0BB3'", "'\\u0BB5\\u0BCD'", 
                     "'\\u0B88'", "'\\u0B8F'", "'\\u0B90'", "'\\u0B92\\u0BB3'", 
                     "'\\u0B9F\\u0BCD'", "'\\u0BB0\\u0BCD'", "'\\u0BB2\\u0BCD'", 
                     "'\\u0BB4\\u0BCD'", "'\\u0BB3\\u0BCD'", "'\\u0BB1\\u0BCD'", 
                     "'\\u0B95\\u0BCD\\u0B95\\u0BCD'", "'\\u0B99\\u0BCD\\u0B99\\u0BCD'", 
                     "'\\u0B9A\\u0BCD\\u0B9A\\u0BCD'", "'\\u0B9E\\u0BCD\\u0B9E\\u0BCD'", 
                     "'\\u0B9F\\u0BCD\\u0B9F\\u0BCD'", "'\\u0BA3\\u0BCD\\u0BA3\\u0BCD'", 
                     "'\\u0BA4\\u0BCD\\u0BA4\\u0BCD'", "'\\u0BA8\\u0BCD\\u0BA8\\u0BCD'", 
                     "'\\u0BAA\\u0BCD\\u0BAA\\u0BCD'", "'\\u0BAE\\u0BCD\\u0BAE\\u0BCD'", 
                     "'\\u0BAF\\u0BCD\\u0BAF\\u0BCD'", "'\\u0BB2\\u0BCD\\u0BB2\\u0BCD'", 
                     "'\\u0BB5\\u0BCD\\u0BB5\\u0BCD'", "'\\u0BB4\\u0BCD\\u0BB4\\u0BCD'", 
                     "'\\u0BB3\\u0BCD\\u0BB3\\u0BCD'", "'\\u0BB1\\u0BCD\\u0BB1\\u0BCD'", 
                     "'\\u0BA9\\u0BCD\\u0BA9\\u0BCD'", "'\\u0B94'", "'\\u0B83'", 
                     "'\\u0B86\\u0B85'", "'\\u0B88\\u0B87'", "'\\u0B8A\\u0B89'", 
                     "'\\u0B8F\\u0B8E'", "'\\u0B90\\u0B87'", "'\\u0B93\\u0B92'", 
                     "'\\u0B94\\u0B89'" ]

    symbolicNames = [  ]

    RULE_சொல் = 0
    RULE_பொதுமொழி = 1
    RULE_ஒர்_எழுத்து_ஒரு_மொழி = 2
    RULE_ஒரெழுத்து = 3
    RULE_மொழிமுதல் = 4
    RULE_மொழியிறுதி = 5
    RULE_மொழியிடை = 6
    RULE_உயிர்மெய்க்குறில் = 7
    RULE_உயிர்மெய்நெடில் = 8
    RULE_சுட்டெழுத்து = 9
    RULE_வினாயெழுத்து = 10
    RULE_ஞகர_முதல் = 11
    RULE_யகர_முதல் = 12
    RULE_வகர_முதல் = 13
    RULE_வேற்றுநிலை_மெய்ம்மயக்கம் = 14
    RULE_ஙகர_வேற்றுநிலை = 15
    RULE_ஞகர_வேற்றுநிலை = 16
    RULE_டகர_வேற்றுநிலை = 17
    RULE_ணகர_வேற்றுநிலை = 18
    RULE_நகர_வேற்றுநிலை = 19
    RULE_மகர_வேற்றுநிலை = 20
    RULE_யகர_வேற்றுநிலை = 21
    RULE_ரகர_வேற்றுநிலை = 22
    RULE_லகர_வேற்றுநிலை = 23
    RULE_வகர_வேற்றுநிலை = 24
    RULE_ழகர_வேற்றுநிலை = 25
    RULE_ளகர_வேற்றுநிலை = 26
    RULE_றகர_வேற்றுநிலை = 27
    RULE_னகர_வேற்றுநிலை = 28
    RULE_உடன்நிலை_மெய்ம்மயக்கம் = 29
    RULE_ஈர்ஒற்று_மயக்கம் = 30
    RULE_உயிர்க்குறில் = 31
    RULE_உயிர்நெடில் = 32
    RULE_ஆய்தம் = 33
    RULE_மெய் = 34
    RULE_வல்லினம் = 35
    RULE_மெல்லினம் = 36
    RULE_இடையினம் = 37
    RULE_உயிரளபெடை_எழுத்து = 38
    RULE_ஒற்றளபெடை_எழுத்து = 39

    ruleNames =  [ "சொல்", "பொதுமொழி", "ஒர்_எழுத்து_ஒரு_மொழி", "ஒரெழுத்து", 
                   "மொழிமுதல்", "மொழியிறுதி", "மொழியிடை", "உயிர்மெய்க்குறில்", 
                   "உயிர்மெய்நெடில்", "சுட்டெழுத்து", "வினாயெழுத்து", "ஞகர_முதல்", 
                   "யகர_முதல்", "வகர_முதல்", "வேற்றுநிலை_மெய்ம்மயக்கம்", 
                   "ஙகர_வேற்றுநிலை", "ஞகர_வேற்றுநிலை", "டகர_வேற்றுநிலை", 
                   "ணகர_வேற்றுநிலை", "நகர_வேற்றுநிலை", "மகர_வேற்றுநிலை", 
                   "யகர_வேற்றுநிலை", "ரகர_வேற்றுநிலை", "லகர_வேற்றுநிலை", 
                   "வகர_வேற்றுநிலை", "ழகர_வேற்றுநிலை", "ளகர_வேற்றுநிலை", 
                   "றகர_வேற்றுநிலை", "னகர_வேற்றுநிலை", "உடன்நிலை_மெய்ம்மயக்கம்", 
                   "ஈர்ஒற்று_மயக்கம்", "உயிர்க்குறில்", "உயிர்நெடில்", "ஆய்தம்", 
                   "மெய்", "வல்லினம்", "மெல்லினம்", "இடையினம்", "உயிரளபெடை_எழுத்து", 
                   "ஒற்றளபெடை_எழுத்து" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    T__50=51
    T__51=52
    T__52=53
    T__53=54
    T__54=55
    T__55=56
    T__56=57
    T__57=58

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class சொல்Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ஒர்_எழுத்து_ஒரு_மொழி(self):
            return self.getTypedRuleContext(சொல்Parser.ஒர்_எழுத்து_ஒரு_மொழிContext,0)


        def பொதுமொழி(self):
            return self.getTypedRuleContext(சொல்Parser.பொதுமொழிContext,0)


        def getRuleIndex(self):
            return சொல்Parser.RULE_சொல்

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterசொல்" ):
                listener.enterசொல்(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitசொல்" ):
                listener.exitசொல்(self)




    def சொல்(self):

        localctx = சொல்Parser.சொல்Context(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_சொல்)
        try:
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.ஒர்_எழுத்து_ஒரு_மொழி()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.பொதுமொழி()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class பொதுமொழிContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def மொழிமுதல்(self):
            return self.getTypedRuleContext(சொல்Parser.மொழிமுதல்Context,0)


        def மொழியிறுதி(self):
            return self.getTypedRuleContext(சொல்Parser.மொழியிறுதிContext,0)


        def மொழியிடை(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(சொல்Parser.மொழியிடைContext)
            else:
                return self.getTypedRuleContext(சொல்Parser.மொழியிடைContext,i)


        def getRuleIndex(self):
            return சொல்Parser.RULE_பொதுமொழி

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterபொதுமொழி" ):
                listener.enterபொதுமொழி(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitபொதுமொழி" ):
                listener.exitபொதுமொழி(self)




    def பொதுமொழி(self):

        localctx = சொல்Parser.பொதுமொழிContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_பொதுமொழி)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.மொழிமுதல்()
            self.state = 88
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 85
                    self.மொழியிடை() 
                self.state = 90
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 91
            self.மொழியிறுதி()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ஒர்_எழுத்து_ஒரு_மொழிContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ஒரெழுத்து(self):
            return self.getTypedRuleContext(சொல்Parser.ஒரெழுத்துContext,0)


        def getRuleIndex(self):
            return சொல்Parser.RULE_ஒர்_எழுத்து_ஒரு_மொழி

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterஒர்_எழுத்து_ஒரு_மொழி" ):
                listener.enterஒர்_எழுத்து_ஒரு_மொழி(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitஒர்_எழுத்து_ஒரு_மொழி" ):
                listener.exitஒர்_எழுத்து_ஒரு_மொழி(self)




    def ஒர்_எழுத்து_ஒரு_மொழி(self):

        localctx = சொல்Parser.ஒர்_எழுத்து_ஒரு_மொழிContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ஒர்_எழுத்து_ஒரு_மொழி)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.ஒரெழுத்து()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ஒரெழுத்துContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def உயிர்மெய்நெடில்(self):
            return self.getTypedRuleContext(சொல்Parser.உயிர்மெய்நெடில்Context,0)


        def உயிர்நெடில்(self):
            return self.getTypedRuleContext(சொல்Parser.உயிர்நெடில்Context,0)


        def getRuleIndex(self):
            return சொல்Parser.RULE_ஒரெழுத்து

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterஒரெழுத்து" ):
                listener.enterஒரெழுத்து(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitஒரெழுத்து" ):
                listener.exitஒரெழுத்து(self)




    def ஒரெழுத்து(self):

        localctx = சொல்Parser.ஒரெழுத்துContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ஒரெழுத்து)
        try:
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 17, 22, 27, 28, 29, 30, 31, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.உயிர்மெய்நெடில்()
                pass
            elif token in [15, 19, 20, 23, 24, 25, 50]:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.உயிர்நெடில்()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class மொழிமுதல்Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def உயிர்க்குறில்(self):
            return self.getTypedRuleContext(சொல்Parser.உயிர்க்குறில்Context,0)


        def உயிர்நெடில்(self):
            return self.getTypedRuleContext(சொல்Parser.உயிர்நெடில்Context,0)


        def ஞகர_முதல்(self):
            return self.getTypedRuleContext(சொல்Parser.ஞகர_முதல்Context,0)


        def யகர_முதல்(self):
            return self.getTypedRuleContext(சொல்Parser.யகர_முதல்Context,0)


        def வகர_முதல்(self):
            return self.getTypedRuleContext(சொல்Parser.வகர_முதல்Context,0)


        def getRuleIndex(self):
            return சொல்Parser.RULE_மொழிமுதல்

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterமொழிமுதல்" ):
                listener.enterமொழிமுதல்(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitமொழிமுதல்" ):
                listener.exitமொழிமுதல்(self)




    def மொழிமுதல்(self):

        localctx = சொல்Parser.மொழிமுதல்Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_மொழிமுதல்)
        self._la = 0 # Token type
        try:
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 14, 16, 18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.உயிர்க்குறில்()
                pass
            elif token in [15, 19, 20, 23, 24, 25, 50]:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.உயிர்நெடில்()
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 101
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 254) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 104
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11, 12, 14, 16, 18]:
                    self.state = 102
                    self.உயிர்க்குறில்()
                    pass
                elif token in [15, 19, 20, 23, 24, 25, 50]:
                    self.state = 103
                    self.உயிர்நெடில்()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 106
                self.ஞகர_முதல்()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 5)
                self.state = 107
                self.யகர_முதல்()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 6)
                self.state = 108
                self.வகர_முதல்()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class மொழியிறுதிContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def உயிர்க்குறில்(self):
            return self.getTypedRuleContext(சொல்Parser.உயிர்க்குறில்Context,0)


        def உயிர்நெடில்(self):
            return self.getTypedRuleContext(சொல்Parser.உயிர்நெடில்Context,0)


        def இடையினம்(self):
            return self.getTypedRuleContext(சொல்Parser.இடையினம்Context,0)


        def getRuleIndex(self):
            return சொல்Parser.RULE_மொழியிறுதி

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterமொழியிறுதி" ):
                listener.enterமொழியிறுதி(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitமொழியிறுதி" ):
                listener.exitமொழியிறுதி(self)




    def மொழியிறுதி(self):

        localctx = சொல்Parser.மொழியிறுதிContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_மொழியிறுதி)
        try:
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 14, 16, 18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.உயிர்க்குறில்()
                pass
            elif token in [15, 19, 20, 23, 24, 25, 50]:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.உயிர்நெடில்()
                pass
            elif token in [5, 7, 8, 9, 10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 113
                self.match(சொல்Parser.T__7)
                pass
            elif token in [17, 22, 28, 29, 30, 31]:
                self.enterOuterAlt(localctx, 4)
                self.state = 131
                self.match(சொல்Parser.T__8)
                pass
            elif token in []:
                self.enterOuterAlt(localctx, 5)
                self.state = 133
                self.match(சொல்Parser.T__4)
                pass
            elif token in []:
                self.enterOuterAlt(localctx, 6)
                self.state = 135
                self.match(சொல்Parser.T__6)
                pass
            elif token in []:
                self.enterOuterAlt(localctx, 7)
                self.state = 137
                self.match(சொல்Parser.T__9)
                pass
            elif token in []:
                self.enterOuterAlt(localctx, 8)
                self.state = 114
                self.இடையினம்()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class மொழியிடைContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def வேற்றுநிலை_மெய்ம்மயக்கம்(self):
            return self.getTypedRuleContext(சொல்Parser.வேற்றுநிலை_மெய்ம்மயக்கம்Context,0)


        def உடன்நிலை_மெய்ம்மயக்கம்(self):
            return self.getTypedRuleContext(சொல்Parser.உடன்நிலை_மெய்ம்மயக்கம்Context,0)


        def ஈர்ஒற்று_மயக்கம்(self):
            return self.getTypedRuleContext(சொல்Parser.ஈர்ஒற்று_மயக்கம்Context,0)


        def getRuleIndex(self):
            return சொல்Parser.RULE_மொழியிடை

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterமொழியிடை" ):
                listener.enterமொழியிடை(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitமொழியிடை" ):
                listener.exitமொழியிடை(self)




    def மொழியிடை(self):

        localctx = சொல்Parser.மொழியிடைContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_மொழியிடை)
        try:
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.வேற்றுநிலை_மெய்ம்மயக்கம்()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.உடன்நிலை_மெய்ம்மயக்கம்()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 119
                self.ஈர்ஒற்று_மயக்கம்()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class உயிர்மெய்க்குறில்Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def மெய்(self):
            return self.getTypedRuleContext(சொல்Parser.மெய்Context,0)


        def உயிர்க்குறில்(self):
            return self.getTypedRuleContext(சொல்Parser.உயிர்க்குறில்Context,0)


        def getRuleIndex(self):
            return சொல்Parser.RULE_உயிர்மெய்க்குறில்

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterஉயிர்மெய்க்குறில்" ):
                listener.enterஉயிர்மெய்க்குறில்(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitஉயிர்மெய்க்குறில்" ):
                listener.exitஉயிர்மெய்க்குறில்(self)




    def உயிர்மெய்க்குறில்(self):

        localctx = சொல்Parser.உயிர்மெய்க்குறில்Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_உயிர்மெய்க்குறில்)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.மெய்()
            self.state = 123
            self.உயிர்க்குறில்()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class உயிர்மெய்நெடில்Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def மெய்(self):
            return self.getTypedRuleContext(சொல்Parser.மெய்Context,0)


        def உயிர்நெடில்(self):
            return self.getTypedRuleContext(சொல்Parser.உயிர்நெடில்Context,0)


        def getRuleIndex(self):
            return சொல்Parser.RULE_உயிர்மெய்நெடில்

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterஉயிர்மெய்நெடில்" ):
                listener.enterஉயிர்மெய்நெடில்(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitஉயிர்மெய்நெடில்" ):
                listener.exitஉயிர்மெய்நெடில்(self)




    def உயிர்மெய்நெடில்(self):

        localctx = சொல்Parser.உயிர்மெய்நெடில்Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_உயிர்மெய்நெடில்)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.மெய்()
            self.state = 126
            self.உயிர்நெடில்()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class சுட்டெழுத்துContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return சொல்Parser.RULE_சுட்டெழுத்து

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterசுட்டெழுத்து" ):
                listener.enterசுட்டெழுத்து(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitசுட்டெழுத்து" ):
                listener.exitசுட்டெழுத்து(self)




    def சுட்டெழுத்து(self):

        localctx = சொல்Parser.சுட்டெழுத்துContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_சுட்டெழுத்து)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class வினாயெழுத்துContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return சொல்Parser.RULE_வினாயெழுத்து

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterவினாயெழுத்து" ):
                listener.enterவினாயெழுத்து(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitவினாயெழுத்து" ):
                listener.exitவினாயெழுத்து(self)




    def வினாயெழுத்து(self):

        localctx = சொல்Parser.வினாயெழுத்துContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_வினாயெழுத்து)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            _la = self._input.LA(1)
            if not(_la==13 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ஞகர_முதல்Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return சொல்Parser.RULE_ஞகர_முதல்

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterஞகர_முதல்" ):
                listener.enterஞகர_முதல்(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitஞகர_முதல்" ):
                listener.exitஞகர_முதல்(self)




    def ஞகர_முதல்(self):

        localctx = சொல்Parser.ஞகர_முதல்Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ஞகர_முதல்)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(சொல்Parser.T__7)
            self.state = 133
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 116736) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class யகர_முதல்Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return சொல்Parser.RULE_யகர_முதல்

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterயகர_முதல்" ):
                listener.enterயகர_முதல்(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitயகர_முதல்" ):
                listener.exitயகர_முதல்(self)




    def யகர_முதல்(self):

        localctx = சொல்Parser.யகர_முதல்Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_யகர_முதல்)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(சொல்Parser.T__16)
            self.state = 136
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3966976) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class வகர_முதல்Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return சொல்Parser.RULE_வகர_முதல்

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterவகர_முதல்" ):
                listener.enterவகர_முதல்(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitவகர_முதல்" ):
                listener.exitவகர_முதல்(self)




    def வகர_முதல்(self):

        localctx = சொல்Parser.வகர_முதல்Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_வகர_முதல்)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(சொல்Parser.T__21)
            self.state = 139
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 125884416) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class வேற்றுநிலை_மெய்ம்மயக்கம்Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ஙகர_வேற்றுநிலை(self):
            return self.getTypedRuleContext(சொல்Parser.ஙகர_வேற்றுநிலைContext,0)


        def ஞகர_வேற்றுநிலை(self):
            return self.getTypedRuleContext(சொல்Parser.ஞகர_வேற்றுநிலைContext,0)


        def டகர_வேற்றுநிலை(self):
            return self.getTypedRuleContext(சொல்Parser.டகர_வேற்றுநிலைContext,0)


        def ணகர_வேற்றுநிலை(self):
            return self.getTypedRuleContext(சொல்Parser.ணகர_வேற்றுநிலைContext,0)


        def நகர_வேற்றுநிலை(self):
            return self.getTypedRuleContext(சொல்Parser.நகர_வேற்றுநிலைContext,0)


        def மகர_வேற்றுநிலை(self):
            return self.getTypedRuleContext(சொல்Parser.மகர_வேற்றுநிலைContext,0)


        def யகர_வேற்றுநிலை(self):
            return self.getTypedRuleContext(சொல்Parser.யகர_வேற்றுநிலைContext,0)


        def ரகர_வேற்றுநிலை(self):
            return self.getTypedRuleContext(சொல்Parser.ரகர_வேற்றுநிலைContext,0)


        def லகர_வேற்றுநிலை(self):
            return self.getTypedRuleContext(சொல்Parser.லகர_வேற்றுநிலைContext,0)


        def வகர_வேற்றுநிலை(self):
            return self.getTypedRuleContext(சொல்Parser.வகர_வேற்றுநிலைContext,0)


        def ழகர_வேற்றுநிலை(self):
            return self.getTypedRuleContext(சொல்Parser.ழகர_வேற்றுநிலைContext,0)


        def ளகர_வேற்றுநிலை(self):
            return self.getTypedRuleContext(சொல்Parser.ளகர_வேற்றுநிலைContext,0)


        def றகர_வேற்றுநிலை(self):
            return self.getTypedRuleContext(சொல்Parser.றகர_வேற்றுநிலைContext,0)


        def னகர_வேற்றுநிலை(self):
            return self.getTypedRuleContext(சொல்Parser.னகர_வேற்றுநிலைContext,0)


        def getRuleIndex(self):
            return சொல்Parser.RULE_வேற்றுநிலை_மெய்ம்மயக்கம்

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterவேற்றுநிலை_மெய்ம்மயக்கம்" ):
                listener.enterவேற்றுநிலை_மெய்ம்மயக்கம்(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitவேற்றுநிலை_மெய்ம்மயக்கம்" ):
                listener.exitவேற்றுநிலை_மெய்ம்மயக்கம்(self)




    def வேற்றுநிலை_மெய்ம்மயக்கம்(self):

        localctx = சொல்Parser.வேற்றுநிலை_மெய்ம்மயக்கம்Context(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_வேற்றுநிலை_மெய்ம்மயக்கம்)
        try:
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.ஙகர_வேற்றுநிலை()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.ஞகர_வேற்றுநிலை()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 3)
                self.state = 143
                self.டகர_வேற்றுநிலை()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 144
                self.ணகர_வேற்றுநிலை()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 145
                self.நகர_வேற்றுநிலை()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 6)
                self.state = 146
                self.மகர_வேற்றுநிலை()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 7)
                self.state = 147
                self.யகர_வேற்றுநிலை()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 8)
                self.state = 148
                self.ரகர_வேற்றுநிலை()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 9)
                self.state = 149
                self.லகர_வேற்றுநிலை()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 10)
                self.state = 150
                self.வகர_வேற்றுநிலை()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 11)
                self.state = 151
                self.ழகர_வேற்றுநிலை()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 12)
                self.state = 152
                self.ளகர_வேற்றுநிலை()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 13)
                self.state = 153
                self.றகர_வேற்றுநிலை()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 14)
                self.state = 154
                self.னகர_வேற்றுநிலை()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ஙகர_வேற்றுநிலைContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return சொல்Parser.RULE_ஙகர_வேற்றுநிலை

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterஙகர_வேற்றுநிலை" ):
                listener.enterஙகர_வேற்றுநிலை(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitஙகர_வேற்றுநிலை" ):
                listener.exitஙகர_வேற்றுநிலை(self)




    def ஙகர_வேற்றுநிலை(self):

        localctx = சொல்Parser.ஙகர_வேற்றுநிலைContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_ஙகர_வேற்றுநிலை)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(சொல்Parser.T__1)

            self.state = 158
            self.match(சொல்Parser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ஞகர_வேற்றுநிலைContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return சொல்Parser.RULE_ஞகர_வேற்றுநிலை

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterஞகர_வேற்றுநிலை" ):
                listener.enterஞகர_வேற்றுநிலை(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitஞகர_வேற்றுநிலை" ):
                listener.exitஞகர_வேற்றுநிலை(self)




    def ஞகர_வேற்றுநிலை(self):

        localctx = சொல்Parser.ஞகர_வேற்றுநிலைContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_ஞகர_வேற்றுநிலை)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(சொல்Parser.T__7)
            self.state = 161
            _la = self._input.LA(1)
            if not(_la==3 or _la==17):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class டகர_வேற்றுநிலைContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return சொல்Parser.RULE_டகர_வேற்றுநிலை

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterடகர_வேற்றுநிலை" ):
                listener.enterடகர_வேற்றுநிலை(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitடகர_வேற்றுநிலை" ):
                listener.exitடகர_வேற்றுநிலை(self)




    def டகர_வேற்றுநிலை(self):

        localctx = சொல்Parser.டகர_வேற்றுநிலைContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_டகர_வேற்றுநிலை)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(சொல்Parser.T__26)
            self.state = 164
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 74) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ணகர_வேற்றுநிலைContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return சொல்Parser.RULE_ணகர_வேற்றுநிலை

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterணகர_வேற்றுநிலை" ):
                listener.enterணகர_வேற்றுநிலை(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitணகர_வேற்றுநிலை" ):
                listener.exitணகர_வேற்றுநிலை(self)




    def ணகர_வேற்றுநிலை(self):

        localctx = சொல்Parser.ணகர_வேற்றுநிலைContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_ணகர_வேற்றுநிலை)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(சொல்Parser.T__8)
            self.state = 167
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 138543562) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class நகர_வேற்றுநிலைContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return சொல்Parser.RULE_நகர_வேற்றுநிலை

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterநகர_வேற்றுநிலை" ):
                listener.enterநகர_வேற்றுநிலை(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitநகர_வேற்றுநிலை" ):
                listener.exitநகர_வேற்றுநிலை(self)




    def நகர_வேற்றுநிலை(self):

        localctx = சொல்Parser.நகர_வேற்றுநிலைContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_நகர_வேற்றுநிலை)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(சொல்Parser.T__4)
            self.state = 170
            _la = self._input.LA(1)
            if not(_la==4 or _la==17):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class மகர_வேற்றுநிலைContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def மெய்(self):
            return self.getTypedRuleContext(சொல்Parser.மெய்Context,0)


        def getRuleIndex(self):
            return சொல்Parser.RULE_மகர_வேற்றுநிலை

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterமகர_வேற்றுநிலை" ):
                listener.enterமகர_வேற்றுநிலை(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitமகர_வேற்றுநிலை" ):
                listener.exitமகர_வேற்றுநிலை(self)




    def மகர_வேற்றுநிலை(self):

        localctx = சொல்Parser.மகர_வேற்றுநிலைContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_மகர_வேற்றுநிலை)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(சொல்Parser.T__6)
            self.state = 173
            self.மெய்()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class யகர_வேற்றுநிலைContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return சொல்Parser.RULE_யகர_வேற்றுநிலை

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterயகர_வேற்றுநிலை" ):
                listener.enterயகர_வேற்றுநிலை(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitயகர_வேற்றுநிலை" ):
                listener.exitயகர_வேற்றுநிலை(self)




    def யகர_வேற்றுநிலை(self):

        localctx = சொல்Parser.யகர_வேற்றுநிலைContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_யகர_வேற்றுநிலை)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(சொல்Parser.T__16)
            self.state = 176
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4194810) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ரகர_வேற்றுநிலைContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return சொல்Parser.RULE_ரகர_வேற்றுநிலை

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterரகர_வேற்றுநிலை" ):
                listener.enterரகர_வேற்றுநிலை(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitரகர_வேற்றுநிலை" ):
                listener.exitரகர_வேற்றுநிலை(self)




    def ரகர_வேற்றுநிலை(self):

        localctx = சொல்Parser.ரகர_வேற்றுநிலைContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_ரகர_வேற்றுநிலை)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(சொல்Parser.T__27)
            self.state = 179
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4194810) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class லகர_வேற்றுநிலைContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return சொல்Parser.RULE_லகர_வேற்றுநிலை

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterலகர_வேற்றுநிலை" ):
                listener.enterலகர_வேற்றுநிலை(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitலகர_வேற்றுநிலை" ):
                listener.exitலகர_வேற்றுநிலை(self)




    def லகர_வேற்றுநிலை(self):

        localctx = சொல்Parser.லகர_வேற்றுநிலைContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_லகர_வேற்றுநிலை)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(சொல்Parser.T__28)
            self.state = 182
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4325450) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class வகர_வேற்றுநிலைContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def மெய்(self):
            return self.getTypedRuleContext(சொல்Parser.மெய்Context,0)


        def getRuleIndex(self):
            return சொல்Parser.RULE_வகர_வேற்றுநிலை

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterவகர_வேற்றுநிலை" ):
                listener.enterவகர_வேற்றுநிலை(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitவகர_வேற்றுநிலை" ):
                listener.exitவகர_வேற்றுநிலை(self)




    def வகர_வேற்றுநிலை(self):

        localctx = சொல்Parser.வகர_வேற்றுநிலைContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_வகர_வேற்றுநிலை)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(சொல்Parser.T__21)
            self.state = 185
            self.மெய்()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ழகர_வேற்றுநிலைContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return சொல்Parser.RULE_ழகர_வேற்றுநிலை

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterழகர_வேற்றுநிலை" ):
                listener.enterழகர_வேற்றுநிலை(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitழகர_வேற்றுநிலை" ):
                listener.exitழகர_வேற்றுநிலை(self)




    def ழகர_வேற்றுநிலை(self):

        localctx = சொல்Parser.ழகர_வேற்றுநிலைContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_ழகர_வேற்றுநிலை)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(சொல்Parser.T__29)
            self.state = 188
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4194810) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ளகர_வேற்றுநிலைContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return சொல்Parser.RULE_ளகர_வேற்றுநிலை

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterளகர_வேற்றுநிலை" ):
                listener.enterளகர_வேற்றுநிலை(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitளகர_வேற்றுநிலை" ):
                listener.exitளகர_வேற்றுநிலை(self)




    def ளகர_வேற்றுநிலை(self):

        localctx = சொல்Parser.ளகர_வேற்றுநிலைContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_ளகர_வேற்றுநிலை)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(சொல்Parser.T__30)
            self.state = 191
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4325450) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class றகர_வேற்றுநிலைContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return சொல்Parser.RULE_றகர_வேற்றுநிலை

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterறகர_வேற்றுநிலை" ):
                listener.enterறகர_வேற்றுநிலை(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitறகர_வேற்றுநிலை" ):
                listener.exitறகர_வேற்றுநிலை(self)




    def றகர_வேற்றுநிலை(self):

        localctx = சொல்Parser.றகர_வேற்றுநிலைContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_றகர_வேற்றுநிலை)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(சொல்Parser.T__31)
            self.state = 194
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 74) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class னகர_வேற்றுநிலைContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return சொல்Parser.RULE_னகர_வேற்றுநிலை

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterனகர_வேற்றுநிலை" ):
                listener.enterனகர_வேற்றுநிலை(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitனகர_வேற்றுநிலை" ):
                listener.exitனகர_வேற்றுநிலை(self)




    def னகர_வேற்றுநிலை(self):

        localctx = சொல்Parser.னகர_வேற்றுநிலைContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_னகர_வேற்றுநிலை)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(சொல்Parser.T__9)
            self.state = 197
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4299293130) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class உடன்நிலை_மெய்ம்மயக்கம்Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return சொல்Parser.RULE_உடன்நிலை_மெய்ம்மயக்கம்

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterஉடன்நிலை_மெய்ம்மயக்கம்" ):
                listener.enterஉடன்நிலை_மெய்ம்மயக்கம்(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitஉடன்நிலை_மெய்ம்மயக்கம்" ):
                listener.exitஉடன்நிலை_மெய்ம்மயக்கம்(self)




    def உடன்நிலை_மெய்ம்மயக்கம்(self):

        localctx = சொல்Parser.உடன்நிலை_மெய்ம்மயக்கம்Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_உடன்நிலை_மெய்ம்மயக்கம்)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1125891316908032) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ஈர்ஒற்று_மயக்கம்Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return சொல்Parser.RULE_ஈர்ஒற்று_மயக்கம்

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterஈர்ஒற்று_மயக்கம்" ):
                listener.enterஈர்ஒற்று_மயக்கம்(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitஈர்ஒற்று_மயக்கம்" ):
                listener.exitஈர்ஒற்று_மயக்கம்(self)




    def ஈர்ஒற்று_மயக்கம்(self):

        localctx = சொல்Parser.ஈர்ஒற்று_மயக்கம்Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_ஈர்ஒற்று_மயக்கம்)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1342308352) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 202
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8375186227200) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class உயிர்க்குறில்Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return சொல்Parser.RULE_உயிர்க்குறில்

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterஉயிர்க்குறில்" ):
                listener.enterஉயிர்க்குறில்(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitஉயிர்க்குறில்" ):
                listener.exitஉயிர்க்குறில்(self)




    def உயிர்க்குறில்(self):

        localctx = சொல்Parser.உயிர்க்குறில்Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_உயிர்க்குறில்)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 350208) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class உயிர்நெடில்Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return சொல்Parser.RULE_உயிர்நெடில்

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterஉயிர்நெடில்" ):
                listener.enterஉயிர்நெடில்(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitஉயிர்நெடில்" ):
                listener.exitஉயிர்நெடில்(self)




    def உயிர்நெடில்(self):

        localctx = சொல்Parser.உயிர்நெடில்Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_உயிர்நெடில்)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1125899967168512) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ஆய்தம்Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return சொல்Parser.RULE_ஆய்தம்

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterஆய்தம்" ):
                listener.enterஆய்தம்(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitஆய்தம்" ):
                listener.exitஆய்தம்(self)




    def ஆய்தம்(self):

        localctx = சொல்Parser.ஆய்தம்Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_ஆய்தம்)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(சொல்Parser.T__50)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class மெய்Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return சொல்Parser.RULE_மெய்

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterமெய்" ):
                listener.enterமெய்(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitமெய்" ):
                listener.exitமெய்(self)




    def மெய்(self):

        localctx = சொல்Parser.மெய்Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_மெய்)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8460044286) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class வல்லினம்Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return சொல்Parser.RULE_வல்லினம்

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterவல்லினம்" ):
                listener.enterவல்லினம்(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitவல்லினம்" ):
                listener.exitவல்லினம்(self)




    def வல்லினம்(self):

        localctx = சொல்Parser.வல்லினம்Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_வல்லினம்)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4429185114) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class மெல்லினம்Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return சொல்Parser.RULE_மெல்லினம்

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterமெல்லினம்" ):
                listener.enterமெல்லினம்(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitமெல்லினம்" ):
                listener.exitமெல்லினம்(self)




    def மெல்லினம்(self):

        localctx = சொல்Parser.மெல்லினம்Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_மெல்லினம்)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1956) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class இடையினம்Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return சொல்Parser.RULE_இடையினம்

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterஇடையினம்" ):
                listener.enterஇடையினம்(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitஇடையினம்" ):
                listener.exitஇடையினம்(self)




    def இடையினம்(self):

        localctx = சொல்Parser.இடையினம்Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_இடையினம்)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4030857216) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class உயிரளபெடை_எழுத்துContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return சொல்Parser.RULE_உயிரளபெடை_எழுத்து

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterஉயிரளபெடை_எழுத்து" ):
                listener.enterஉயிரளபெடை_எழுத்து(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitஉயிரளபெடை_எழுத்து" ):
                listener.exitஉயிரளபெடை_எழுத்து(self)




    def உயிரளபெடை_எழுத்து(self):

        localctx = சொல்Parser.உயிரளபெடை_எழுத்துContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_உயிரளபெடை_எழுத்து)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 571957152676052992) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ஒற்றளபெடை_எழுத்துContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return சொல்Parser.RULE_ஒற்றளபெடை_எழுத்து

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterஒற்றளபெடை_எழுத்து" ):
                listener.enterஒற்றளபெடை_எழுத்து(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitஒற்றளபெடை_எழுத்து" ):
                listener.exitஒற்றளபெடை_எழுத்து(self)




    def ஒற்றளபெடை_எழுத்து(self):

        localctx = சொல்Parser.ஒற்றளபெடை_எழுத்துContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_ஒற்றளபெடை_எழுத்து)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2251802502367140) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





