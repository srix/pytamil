# Generated from /home/srix/Documents/tamil-research/pytamil/pytamil/தமிழ்/resources/புணர்ச்சிவிதிகள்.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("I\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\7\2\32\n\2")
        buf.write("\f\2\16\2\35\13\2\3\3\3\3\3\3\3\3\3\4\3\4\7\4%\n\4\f\4")
        buf.write("\16\4(\13\4\3\5\7\5+\n\5\f\5\16\5.\13\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\5\6\67\n\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\n\6\nC\n\n\r\n\16\nD\3\13\3\13\3\13\2\2\f\2")
        buf.write("\4\6\b\n\f\16\20\22\24\2\4\3\2\t\f\3\2\r\16\2C\2\26\3")
        buf.write("\2\2\2\4\36\3\2\2\2\6\"\3\2\2\2\b,\3\2\2\2\n\66\3\2\2")
        buf.write("\2\f8\3\2\2\2\16;\3\2\2\2\20?\3\2\2\2\22B\3\2\2\2\24F")
        buf.write("\3\2\2\2\26\33\5\4\3\2\27\30\7\3\2\2\30\32\5\4\3\2\31")
        buf.write("\27\3\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2")
        buf.write("\34\3\3\2\2\2\35\33\3\2\2\2\36\37\5\6\4\2\37 \5\24\13")
        buf.write("\2 !\5\b\5\2!\5\3\2\2\2\"&\7\4\2\2#%\5\n\6\2$#\3\2\2\2")
        buf.write("%(\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'\7\3\2\2\2(&\3\2\2\2")
        buf.write(")+\5\n\6\2*)\3\2\2\2+.\3\2\2\2,*\3\2\2\2,-\3\2\2\2-/\3")
        buf.write("\2\2\2.,\3\2\2\2/\60\7\5\2\2\60\t\3\2\2\2\61\62\7\6\2")
        buf.write("\2\62\67\5\f\7\2\63\64\5\f\7\2\64\65\7\6\2\2\65\67\3\2")
        buf.write("\2\2\66\61\3\2\2\2\66\63\3\2\2\2\67\13\3\2\2\289\5\20")
        buf.write("\t\29:\5\16\b\2:\r\3\2\2\2;<\7\7\2\2<=\5\22\n\2=>\7\b")
        buf.write("\2\2>\17\3\2\2\2?@\t\2\2\2@\21\3\2\2\2AC\t\3\2\2BA\3\2")
        buf.write("\2\2CD\3\2\2\2DB\3\2\2\2DE\3\2\2\2E\23\3\2\2\2FG\7\17")
        buf.write("\2\2G\25\3\2\2\2\7\33&,\66D")
        return buf.getvalue()


class புணர்ச்சிவிதிகள்Parser ( Parser ):

    grammarFileName = "புணர்ச்சிவிதிகள்.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'\u0BA8\u0BBF\u0BB2\u0BC8\u0BAE\u0BCA\u0BB4\u0BBF'", 
                     "'\u0BB5\u0BB0\u0BC1\u0BAE\u0BCA\u0BB4\u0BBF'", "'|'", 
                     "'('", "')'", "'\u0B89\u0B9F\u0BAE\u0BCD\u0BAA\u0B9F\u0BC1\u0BAE\u0BC6\u0BAF\u0BCD'", 
                     "'\u0B87\u0BB0\u0B9F\u0BCD\u0B9F\u0BC1\u0BA4\u0BB2\u0BCD'", 
                     "'\u0BA4\u0BBF\u0BB0\u0BBF\u0BA4\u0BB2\u0BCD'", "'\u0B9A\u0BC1\u0BAE\u0BCD\u0BAE\u0BBE'", 
                     "'\u0BB5\u0BCD'", "'\u0BAF\u0BCD'", "'+'" ]

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
        self.checkVersion("4.9.2")
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
            while _la==புணர்ச்சிவிதிகள்Parser.T__0:
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << புணர்ச்சிவிதிகள்Parser.T__3) | (1 << புணர்ச்சிவிதிகள்Parser.T__6) | (1 << புணர்ச்சிவிதிகள்Parser.T__7) | (1 << புணர்ச்சிவிதிகள்Parser.T__8) | (1 << புணர்ச்சிவிதிகள்Parser.T__9))) != 0):
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << புணர்ச்சிவிதிகள்Parser.T__3) | (1 << புணர்ச்சிவிதிகள்Parser.T__6) | (1 << புணர்ச்சிவிதிகள்Parser.T__7) | (1 << புணர்ச்சிவிதிகள்Parser.T__8) | (1 << புணர்ச்சிவிதிகள்Parser.T__9))) != 0):
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
            if token in [புணர்ச்சிவிதிகள்Parser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(புணர்ச்சிவிதிகள்Parser.T__3)
                self.state = 48
                self.fil()
                pass
            elif token in [புணர்ச்சிவிதிகள்Parser.T__6, புணர்ச்சிவிதிகள்Parser.T__7, புணர்ச்சிவிதிகள்Parser.T__8, புணர்ச்சிவிதிகள்Parser.T__9]:
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
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << புணர்ச்சிவிதிகள்Parser.T__6) | (1 << புணர்ச்சிவிதிகள்Parser.T__7) | (1 << புணர்ச்சிவிதிகள்Parser.T__8) | (1 << புணர்ச்சிவிதிகள்Parser.T__9))) != 0)):
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
                if not(_la==புணர்ச்சிவிதிகள்Parser.T__10 or _la==புணர்ச்சிவிதிகள்Parser.T__11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 66 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==புணர்ச்சிவிதிகள்Parser.T__10 or _la==புணர்ச்சிவிதிகள்Parser.T__11):
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





