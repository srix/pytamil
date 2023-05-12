# Generated from /home/srix/workspace/pytamil-all/pytamil-3.10/pytamil/தமிழ்/resources/புணர்ச்சிவிதிகள்.g4 by ANTLR 4.12.0
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
        4,1,13,71,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,5,0,24,8,0,10,0,12,0,27,9,
        0,1,1,1,1,1,1,1,1,1,2,1,2,5,2,35,8,2,10,2,12,2,38,9,2,1,3,5,3,41,
        8,3,10,3,12,3,44,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,3,4,53,8,4,1,5,
        1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,8,4,8,65,8,8,11,8,12,8,66,1,9,
        1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,2,1,0,7,10,1,0,11,12,65,
        0,20,1,0,0,0,2,28,1,0,0,0,4,32,1,0,0,0,6,42,1,0,0,0,8,52,1,0,0,0,
        10,54,1,0,0,0,12,57,1,0,0,0,14,61,1,0,0,0,16,64,1,0,0,0,18,68,1,
        0,0,0,20,25,3,2,1,0,21,22,5,1,0,0,22,24,3,2,1,0,23,21,1,0,0,0,24,
        27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,1,1,0,0,0,27,25,1,0,0,
        0,28,29,3,4,2,0,29,30,3,18,9,0,30,31,3,6,3,0,31,3,1,0,0,0,32,36,
        5,2,0,0,33,35,3,8,4,0,34,33,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,
        36,37,1,0,0,0,37,5,1,0,0,0,38,36,1,0,0,0,39,41,3,8,4,0,40,39,1,0,
        0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,45,1,0,0,0,44,42,
        1,0,0,0,45,46,5,3,0,0,46,7,1,0,0,0,47,48,5,4,0,0,48,53,3,10,5,0,
        49,50,3,10,5,0,50,51,5,4,0,0,51,53,1,0,0,0,52,47,1,0,0,0,52,49,1,
        0,0,0,53,9,1,0,0,0,54,55,3,14,7,0,55,56,3,12,6,0,56,11,1,0,0,0,57,
        58,5,5,0,0,58,59,3,16,8,0,59,60,5,6,0,0,60,13,1,0,0,0,61,62,7,0,
        0,0,62,15,1,0,0,0,63,65,7,1,0,0,64,63,1,0,0,0,65,66,1,0,0,0,66,64,
        1,0,0,0,66,67,1,0,0,0,67,17,1,0,0,0,68,69,5,13,0,0,69,19,1,0,0,0,
        5,25,36,42,52,66
    ]

class புணர்ச்சிவிதிகள்Parser ( Parser ):

    grammarFileName = "புணர்ச்சிவிதிகள்.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'\\u0BA8\\u0BBF\\u0BB2\\u0BC8\\u0BAE\\u0BCA\\u0BB4\\u0BBF'", 
                     "'\\u0BB5\\u0BB0\\u0BC1\\u0BAE\\u0BCA\\u0BB4\\u0BBF'", 
                     "'|'", "'('", "')'", "'\\u0B89\\u0B9F\\u0BAE\\u0BCD\\u0BAA\\u0B9F\\u0BC1\\u0BAE\\u0BC6\\u0BAF\\u0BCD'", 
                     "'\\u0B87\\u0BB0\\u0B9F\\u0BCD\\u0B9F\\u0BC1\\u0BA4\\u0BB2\\u0BCD'", 
                     "'\\u0BA4\\u0BBF\\u0BB0\\u0BBF\\u0BA4\\u0BB2\\u0BCD'", 
                     "'\\u0B9A\\u0BC1\\u0BAE\\u0BCD\\u0BAE\\u0BBE'", "'\\u0BB5\\u0BCD'", 
                     "'\\u0BAF\\u0BCD'", "'+'" ]

    symbolicNames = [  ]

    RULE_புணர்ச்சிவிதிகள் = 0
    RULE_விதி = 1
    RULE_நிலைமொழி_மாற்றம் = 2
    RULE_வருமொழி_மாற்றம் = 3
    RULE_filters = 4
    RULE_fil = 5
    RULE_param = 6
    RULE_filtername = 7
    RULE_value = 8
    RULE_கூட்டல் = 9

    ruleNames =  [ "புணர்ச்சிவிதிகள்", "விதி", "நிலைமொழி_மாற்றம்", "வருமொழி_மாற்றம்", 
                   "filters", "fil", "param", "filtername", "value", "கூட்டல்" ]

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

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class புணர்ச்சிவிதிகள்Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def விதி(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(புணர்ச்சிவிதிகள்Parser.விதிContext)
            else:
                return self.getTypedRuleContext(புணர்ச்சிவிதிகள்Parser.விதிContext,i)


        def getRuleIndex(self):
            return புணர்ச்சிவிதிகள்Parser.RULE_புணர்ச்சிவிதிகள்

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterபுணர்ச்சிவிதிகள்" ):
                listener.enterபுணர்ச்சிவிதிகள்(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitபுணர்ச்சிவிதிகள்" ):
                listener.exitபுணர்ச்சிவிதிகள்(self)




    def புணர்ச்சிவிதிகள்(self):

        localctx = புணர்ச்சிவிதிகள்Parser.புணர்ச்சிவிதிகள்Context(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_புணர்ச்சிவிதிகள்)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.விதி()
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 21
                self.match(புணர்ச்சிவிதிகள்Parser.T__0)
                self.state = 22
                self.விதி()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class விதிContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def நிலைமொழி_மாற்றம்(self):
            return self.getTypedRuleContext(புணர்ச்சிவிதிகள்Parser.நிலைமொழி_மாற்றம்Context,0)


        def கூட்டல்(self):
            return self.getTypedRuleContext(புணர்ச்சிவிதிகள்Parser.கூட்டல்Context,0)


        def வருமொழி_மாற்றம்(self):
            return self.getTypedRuleContext(புணர்ச்சிவிதிகள்Parser.வருமொழி_மாற்றம்Context,0)


        def getRuleIndex(self):
            return புணர்ச்சிவிதிகள்Parser.RULE_விதி

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterவிதி" ):
                listener.enterவிதி(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitவிதி" ):
                listener.exitவிதி(self)




    def விதி(self):

        localctx = புணர்ச்சிவிதிகள்Parser.விதிContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_விதி)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.நிலைமொழி_மாற்றம்()
            self.state = 29
            self.கூட்டல்()
            self.state = 30
            self.வருமொழி_மாற்றம்()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class நிலைமொழி_மாற்றம்Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def filters(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(புணர்ச்சிவிதிகள்Parser.FiltersContext)
            else:
                return self.getTypedRuleContext(புணர்ச்சிவிதிகள்Parser.FiltersContext,i)


        def getRuleIndex(self):
            return புணர்ச்சிவிதிகள்Parser.RULE_நிலைமொழி_மாற்றம்

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterநிலைமொழி_மாற்றம்" ):
                listener.enterநிலைமொழி_மாற்றம்(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitநிலைமொழி_மாற்றம்" ):
                listener.exitநிலைமொழி_மாற்றம்(self)




    def நிலைமொழி_மாற்றம்(self):

        localctx = புணர்ச்சிவிதிகள்Parser.நிலைமொழி_மாற்றம்Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_நிலைமொழி_மாற்றம்)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(புணர்ச்சிவிதிகள்Parser.T__1)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1936) != 0):
                self.state = 33
                self.filters()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class வருமொழி_மாற்றம்Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def filters(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(புணர்ச்சிவிதிகள்Parser.FiltersContext)
            else:
                return self.getTypedRuleContext(புணர்ச்சிவிதிகள்Parser.FiltersContext,i)


        def getRuleIndex(self):
            return புணர்ச்சிவிதிகள்Parser.RULE_வருமொழி_மாற்றம்

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterவருமொழி_மாற்றம்" ):
                listener.enterவருமொழி_மாற்றம்(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitவருமொழி_மாற்றம்" ):
                listener.exitவருமொழி_மாற்றம்(self)




    def வருமொழி_மாற்றம்(self):

        localctx = புணர்ச்சிவிதிகள்Parser.வருமொழி_மாற்றம்Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_வருமொழி_மாற்றம்)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1936) != 0):
                self.state = 39
                self.filters()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self.match(புணர்ச்சிவிதிகள்Parser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FiltersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fil(self):
            return self.getTypedRuleContext(புணர்ச்சிவிதிகள்Parser.FilContext,0)


        def getRuleIndex(self):
            return புணர்ச்சிவிதிகள்Parser.RULE_filters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilters" ):
                listener.enterFilters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilters" ):
                listener.exitFilters(self)




    def filters(self):

        localctx = புணர்ச்சிவிதிகள்Parser.FiltersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_filters)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(புணர்ச்சிவிதிகள்Parser.T__3)
                self.state = 48
                self.fil()
                pass
            elif token in [7, 8, 9, 10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.fil()
                self.state = 50
                self.match(புணர்ச்சிவிதிகள்Parser.T__3)
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


    class FilContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def filtername(self):
            return self.getTypedRuleContext(புணர்ச்சிவிதிகள்Parser.FilternameContext,0)


        def param(self):
            return self.getTypedRuleContext(புணர்ச்சிவிதிகள்Parser.ParamContext,0)


        def getRuleIndex(self):
            return புணர்ச்சிவிதிகள்Parser.RULE_fil

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFil" ):
                listener.enterFil(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFil" ):
                listener.exitFil(self)




    def fil(self):

        localctx = புணர்ச்சிவிதிகள்Parser.FilContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_fil)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.filtername()
            self.state = 55
            self.param()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(புணர்ச்சிவிதிகள்Parser.ValueContext,0)


        def getRuleIndex(self):
            return புணர்ச்சிவிதிகள்Parser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)




    def param(self):

        localctx = புணர்ச்சிவிதிகள்Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(புணர்ச்சிவிதிகள்Parser.T__4)
            self.state = 58
            self.value()
            self.state = 59
            self.match(புணர்ச்சிவிதிகள்Parser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilternameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return புணர்ச்சிவிதிகள்Parser.RULE_filtername

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFiltername" ):
                listener.enterFiltername(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFiltername" ):
                listener.exitFiltername(self)




    def filtername(self):

        localctx = புணர்ச்சிவிதிகள்Parser.FilternameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_filtername)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1920) != 0)):
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


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return புணர்ச்சிவிதிகள்Parser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = புணர்ச்சிவிதிகள்Parser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 63
                _la = self._input.LA(1)
                if not(_la==11 or _la==12):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 66 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==11 or _la==12):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class கூட்டல்Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return புணர்ச்சிவிதிகள்Parser.RULE_கூட்டல்

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterகூட்டல்" ):
                listener.enterகூட்டல்(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitகூட்டல்" ):
                listener.exitகூட்டல்(self)




    def கூட்டல்(self):

        localctx = புணர்ச்சிவிதிகள்Parser.கூட்டல்Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_கூட்டல்)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(புணர்ச்சிவிதிகள்Parser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





