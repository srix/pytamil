# Generated from /home/srix/workspace/pytamil/pytamil/தமிழ்/resources/மாத்திரை.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3(")
        buf.write("P\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\3\2\3\2\7\2\37\n\2\f\2\16\2\"\13\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\5\3*\n\3\3\4\3\4\3\4\3\4\5\4\60\n\4\3\5\3\5\5")
        buf.write("\5\64\n\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6<\n\6\3\7\3\7\3\b")
        buf.write("\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\16\3\16\3\16\2\2\17\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\2\7\3\2\3\7\3\2\b\16\3\2\17 \3\2\"(\5\2\25\33\35\36")
        buf.write(" !\2K\2\34\3\2\2\2\4)\3\2\2\2\6/\3\2\2\2\b\63\3\2\2\2")
        buf.write("\n;\3\2\2\2\f=\3\2\2\2\16?\3\2\2\2\20A\3\2\2\2\22C\3\2")
        buf.write("\2\2\24E\3\2\2\2\26H\3\2\2\2\30K\3\2\2\2\32M\3\2\2\2\34")
        buf.write(" \5\4\3\2\35\37\5\6\4\2\36\35\3\2\2\2\37\"\3\2\2\2 \36")
        buf.write("\3\2\2\2 !\3\2\2\2!#\3\2\2\2\" \3\2\2\2#$\5\b\5\2$\3\3")
        buf.write("\2\2\2%*\5\f\7\2&*\5\16\b\2\'*\5\24\13\2(*\5\26\f\2)%")
        buf.write("\3\2\2\2)&\3\2\2\2)\'\3\2\2\2)(\3\2\2\2*\5\3\2\2\2+\60")
        buf.write("\5\24\13\2,\60\5\26\f\2-\60\5\20\t\2.\60\5\22\n\2/+\3")
        buf.write("\2\2\2/,\3\2\2\2/-\3\2\2\2/.\3\2\2\2\60\7\3\2\2\2\61\64")
        buf.write("\5\24\13\2\62\64\5\20\t\2\63\61\3\2\2\2\63\62\3\2\2\2")
        buf.write("\64\t\3\2\2\2\65\66\5\f\7\2\66\67\5\24\13\2\67<\3\2\2")
        buf.write("\289\5\24\13\29:\5\24\13\2:<\3\2\2\2;\65\3\2\2\2;8\3\2")
        buf.write("\2\2<\13\3\2\2\2=>\t\2\2\2>\r\3\2\2\2?@\t\3\2\2@\17\3")
        buf.write("\2\2\2AB\t\4\2\2B\21\3\2\2\2CD\7!\2\2D\23\3\2\2\2EF\5")
        buf.write("\20\t\2FG\5\f\7\2G\25\3\2\2\2HI\5\20\t\2IJ\5\16\b\2J\27")
        buf.write("\3\2\2\2KL\t\5\2\2L\31\3\2\2\2MN\t\6\2\2N\33\3\2\2\2\7")
        buf.write(" )/\63;")
        return buf.getvalue()


class மாத்திரைParser ( Parser ):

    grammarFileName = "மாத்திரை.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\u0B85'", "'\u0B87'", "'\u0B89'", "'\u0B8E'", 
                     "'\u0B92'", "'\u0B86'", "'\u0B88'", "'\u0B8A'", "'\u0B8F'", 
                     "'\u0B90'", "'\u0B93'", "'\u0B92\u0BB3'", "'\u0B95\u0BCD'", 
                     "'\u0B9A\u0BCD'", "'\u0B9F\u0BCD'", "'\u0BA4\u0BCD'", 
                     "'\u0BAA\u0BCD'", "'\u0BB1\u0BCD'", "'\u0B9E\u0BCD'", 
                     "'\u0B99\u0BCD'", "'\u0BA3\u0BCD'", "'\u0BA8\u0BCD'", 
                     "'\u0BAE\u0BCD'", "'\u0BA9\u0BCD'", "'\u0BAF\u0BCD'", 
                     "'\u0BB0\u0BCD'", "'\u0BB2\u0BCD'", "'\u0BB5\u0BCD'", 
                     "'\u0BB4\u0BCD'", "'\u0BB3\u0BCD'", "'\u0B83'", "'\u0B86\u0B85'", 
                     "'\u0B88\u0B87'", "'\u0B8A\u0B89'", "'\u0B8F\u0B8E'", 
                     "'\u0B90\u0B87'", "'\u0B93\u0B92'", "'\u0B92\u0BB3\u0B89'" ]

    symbolicNames = [  ]

    RULE_மாத்திரை = 0
    RULE_மொழிமுதல் = 1
    RULE_மொழியிடை = 2
    RULE_மொழியிறுதி = 3
    RULE_குறிலிணை = 4
    RULE_உயிர்க்குறில் = 5
    RULE_உயிர்நெடில் = 6
    RULE_மெய் = 7
    RULE_ஆய்தம் = 8
    RULE_உயிர்மெய்க்குறில் = 9
    RULE_உயிர்மெய்நெடில் = 10
    RULE_உயிரளபெடை = 11
    RULE_ஒற்றளபெடை = 12

    ruleNames =  [ "மாத்திரை", "மொழிமுதல்", "மொழியிடை", "மொழியிறுதி", "குறிலிணை", 
                   "உயிர்க்குறில்", "உயிர்நெடில்", "மெய்", "ஆய்தம்", "உயிர்மெய்க்குறில்", 
                   "உயிர்மெய்நெடில்", "உயிரளபெடை", "ஒற்றளபெடை" ]

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

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class மாத்திரைContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def மொழிமுதல்(self):
            return self.getTypedRuleContext(மாத்திரைParser.மொழிமுதல்Context,0)


        def மொழியிறுதி(self):
            return self.getTypedRuleContext(மாத்திரைParser.மொழியிறுதிContext,0)


        def மொழியிடை(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(மாத்திரைParser.மொழியிடைContext)
            else:
                return self.getTypedRuleContext(மாத்திரைParser.மொழியிடைContext,i)


        def getRuleIndex(self):
            return மாத்திரைParser.RULE_மாத்திரை

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterமாத்திரை" ):
                listener.enterமாத்திரை(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitமாத்திரை" ):
                listener.exitமாத்திரை(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitமாத்திரை" ):
                return visitor.visitமாத்திரை(self)
            else:
                return visitor.visitChildren(self)




    def மாத்திரை(self):

        localctx = மாத்திரைParser.மாத்திரைContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_மாத்திரை)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.மொழிமுதல்()
            self.state = 30
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 27
                    self.மொழியிடை() 
                self.state = 32
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 33
            self.மொழியிறுதி()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class மொழிமுதல்Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def உயிர்க்குறில்(self):
            return self.getTypedRuleContext(மாத்திரைParser.உயிர்க்குறில்Context,0)


        def உயிர்நெடில்(self):
            return self.getTypedRuleContext(மாத்திரைParser.உயிர்நெடில்Context,0)


        def உயிர்மெய்க்குறில்(self):
            return self.getTypedRuleContext(மாத்திரைParser.உயிர்மெய்க்குறில்Context,0)


        def உயிர்மெய்நெடில்(self):
            return self.getTypedRuleContext(மாத்திரைParser.உயிர்மெய்நெடில்Context,0)


        def getRuleIndex(self):
            return மாத்திரைParser.RULE_மொழிமுதல்

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterமொழிமுதல்" ):
                listener.enterமொழிமுதல்(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitமொழிமுதல்" ):
                listener.exitமொழிமுதல்(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitமொழிமுதல்" ):
                return visitor.visitமொழிமுதல்(self)
            else:
                return visitor.visitChildren(self)




    def மொழிமுதல்(self):

        localctx = மாத்திரைParser.மொழிமுதல்Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_மொழிமுதல்)
        try:
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.உயிர்க்குறில்()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.உயிர்நெடில்()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.உயிர்மெய்க்குறில்()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 38
                self.உயிர்மெய்நெடில்()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class மொழியிடைContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def உயிர்மெய்க்குறில்(self):
            return self.getTypedRuleContext(மாத்திரைParser.உயிர்மெய்க்குறில்Context,0)


        def உயிர்மெய்நெடில்(self):
            return self.getTypedRuleContext(மாத்திரைParser.உயிர்மெய்நெடில்Context,0)


        def மெய்(self):
            return self.getTypedRuleContext(மாத்திரைParser.மெய்Context,0)


        def ஆய்தம்(self):
            return self.getTypedRuleContext(மாத்திரைParser.ஆய்தம்Context,0)


        def getRuleIndex(self):
            return மாத்திரைParser.RULE_மொழியிடை

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterமொழியிடை" ):
                listener.enterமொழியிடை(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitமொழியிடை" ):
                listener.exitமொழியிடை(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitமொழியிடை" ):
                return visitor.visitமொழியிடை(self)
            else:
                return visitor.visitChildren(self)




    def மொழியிடை(self):

        localctx = மாத்திரைParser.மொழியிடைContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_மொழியிடை)
        try:
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.உயிர்மெய்க்குறில்()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.உயிர்மெய்நெடில்()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.மெய்()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 44
                self.ஆய்தம்()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class மொழியிறுதிContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def உயிர்மெய்க்குறில்(self):
            return self.getTypedRuleContext(மாத்திரைParser.உயிர்மெய்க்குறில்Context,0)


        def மெய்(self):
            return self.getTypedRuleContext(மாத்திரைParser.மெய்Context,0)


        def getRuleIndex(self):
            return மாத்திரைParser.RULE_மொழியிறுதி

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterமொழியிறுதி" ):
                listener.enterமொழியிறுதி(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitமொழியிறுதி" ):
                listener.exitமொழியிறுதி(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitமொழியிறுதி" ):
                return visitor.visitமொழியிறுதி(self)
            else:
                return visitor.visitChildren(self)




    def மொழியிறுதி(self):

        localctx = மாத்திரைParser.மொழியிறுதிContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_மொழியிறுதி)
        try:
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.உயிர்மெய்க்குறில்()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.மெய்()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class குறிலிணைContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def உயிர்க்குறில்(self):
            return self.getTypedRuleContext(மாத்திரைParser.உயிர்க்குறில்Context,0)


        def உயிர்மெய்க்குறில்(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(மாத்திரைParser.உயிர்மெய்க்குறில்Context)
            else:
                return self.getTypedRuleContext(மாத்திரைParser.உயிர்மெய்க்குறில்Context,i)


        def getRuleIndex(self):
            return மாத்திரைParser.RULE_குறிலிணை

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterகுறிலிணை" ):
                listener.enterகுறிலிணை(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitகுறிலிணை" ):
                listener.exitகுறிலிணை(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitகுறிலிணை" ):
                return visitor.visitகுறிலிணை(self)
            else:
                return visitor.visitChildren(self)




    def குறிலிணை(self):

        localctx = மாத்திரைParser.குறிலிணைContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_குறிலிணை)
        try:
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [மாத்திரைParser.T__0, மாத்திரைParser.T__1, மாத்திரைParser.T__2, மாத்திரைParser.T__3, மாத்திரைParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.உயிர்க்குறில்()
                self.state = 52
                self.உயிர்மெய்க்குறில்()
                pass
            elif token in [மாத்திரைParser.T__12, மாத்திரைParser.T__13, மாத்திரைParser.T__14, மாத்திரைParser.T__15, மாத்திரைParser.T__16, மாத்திரைParser.T__17, மாத்திரைParser.T__18, மாத்திரைParser.T__19, மாத்திரைParser.T__20, மாத்திரைParser.T__21, மாத்திரைParser.T__22, மாத்திரைParser.T__23, மாத்திரைParser.T__24, மாத்திரைParser.T__25, மாத்திரைParser.T__26, மாத்திரைParser.T__27, மாத்திரைParser.T__28, மாத்திரைParser.T__29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.உயிர்மெய்க்குறில்()
                self.state = 55
                self.உயிர்மெய்க்குறில்()
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

    class உயிர்க்குறில்Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return மாத்திரைParser.RULE_உயிர்க்குறில்

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterஉயிர்க்குறில்" ):
                listener.enterஉயிர்க்குறில்(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitஉயிர்க்குறில்" ):
                listener.exitஉயிர்க்குறில்(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitஉயிர்க்குறில்" ):
                return visitor.visitஉயிர்க்குறில்(self)
            else:
                return visitor.visitChildren(self)




    def உயிர்க்குறில்(self):

        localctx = மாத்திரைParser.உயிர்க்குறில்Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_உயிர்க்குறில்)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << மாத்திரைParser.T__0) | (1 << மாத்திரைParser.T__1) | (1 << மாத்திரைParser.T__2) | (1 << மாத்திரைParser.T__3) | (1 << மாத்திரைParser.T__4))) != 0)):
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return மாத்திரைParser.RULE_உயிர்நெடில்

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterஉயிர்நெடில்" ):
                listener.enterஉயிர்நெடில்(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitஉயிர்நெடில்" ):
                listener.exitஉயிர்நெடில்(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitஉயிர்நெடில்" ):
                return visitor.visitஉயிர்நெடில்(self)
            else:
                return visitor.visitChildren(self)




    def உயிர்நெடில்(self):

        localctx = மாத்திரைParser.உயிர்நெடில்Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_உயிர்நெடில்)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << மாத்திரைParser.T__5) | (1 << மாத்திரைParser.T__6) | (1 << மாத்திரைParser.T__7) | (1 << மாத்திரைParser.T__8) | (1 << மாத்திரைParser.T__9) | (1 << மாத்திரைParser.T__10) | (1 << மாத்திரைParser.T__11))) != 0)):
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

    class மெய்Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return மாத்திரைParser.RULE_மெய்

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterமெய்" ):
                listener.enterமெய்(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitமெய்" ):
                listener.exitமெய்(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitமெய்" ):
                return visitor.visitமெய்(self)
            else:
                return visitor.visitChildren(self)




    def மெய்(self):

        localctx = மாத்திரைParser.மெய்Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_மெய்)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << மாத்திரைParser.T__12) | (1 << மாத்திரைParser.T__13) | (1 << மாத்திரைParser.T__14) | (1 << மாத்திரைParser.T__15) | (1 << மாத்திரைParser.T__16) | (1 << மாத்திரைParser.T__17) | (1 << மாத்திரைParser.T__18) | (1 << மாத்திரைParser.T__19) | (1 << மாத்திரைParser.T__20) | (1 << மாத்திரைParser.T__21) | (1 << மாத்திரைParser.T__22) | (1 << மாத்திரைParser.T__23) | (1 << மாத்திரைParser.T__24) | (1 << மாத்திரைParser.T__25) | (1 << மாத்திரைParser.T__26) | (1 << மாத்திரைParser.T__27) | (1 << மாத்திரைParser.T__28) | (1 << மாத்திரைParser.T__29))) != 0)):
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return மாத்திரைParser.RULE_ஆய்தம்

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterஆய்தம்" ):
                listener.enterஆய்தம்(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitஆய்தம்" ):
                listener.exitஆய்தம்(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitஆய்தம்" ):
                return visitor.visitஆய்தம்(self)
            else:
                return visitor.visitChildren(self)




    def ஆய்தம்(self):

        localctx = மாத்திரைParser.ஆய்தம்Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ஆய்தம்)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(மாத்திரைParser.T__30)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class உயிர்மெய்க்குறில்Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def மெய்(self):
            return self.getTypedRuleContext(மாத்திரைParser.மெய்Context,0)


        def உயிர்க்குறில்(self):
            return self.getTypedRuleContext(மாத்திரைParser.உயிர்க்குறில்Context,0)


        def getRuleIndex(self):
            return மாத்திரைParser.RULE_உயிர்மெய்க்குறில்

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterஉயிர்மெய்க்குறில்" ):
                listener.enterஉயிர்மெய்க்குறில்(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitஉயிர்மெய்க்குறில்" ):
                listener.exitஉயிர்மெய்க்குறில்(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitஉயிர்மெய்க்குறில்" ):
                return visitor.visitஉயிர்மெய்க்குறில்(self)
            else:
                return visitor.visitChildren(self)




    def உயிர்மெய்க்குறில்(self):

        localctx = மாத்திரைParser.உயிர்மெய்க்குறில்Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_உயிர்மெய்க்குறில்)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.மெய்()
            self.state = 68
            self.உயிர்க்குறில்()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class உயிர்மெய்நெடில்Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def மெய்(self):
            return self.getTypedRuleContext(மாத்திரைParser.மெய்Context,0)


        def உயிர்நெடில்(self):
            return self.getTypedRuleContext(மாத்திரைParser.உயிர்நெடில்Context,0)


        def getRuleIndex(self):
            return மாத்திரைParser.RULE_உயிர்மெய்நெடில்

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterஉயிர்மெய்நெடில்" ):
                listener.enterஉயிர்மெய்நெடில்(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitஉயிர்மெய்நெடில்" ):
                listener.exitஉயிர்மெய்நெடில்(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitஉயிர்மெய்நெடில்" ):
                return visitor.visitஉயிர்மெய்நெடில்(self)
            else:
                return visitor.visitChildren(self)




    def உயிர்மெய்நெடில்(self):

        localctx = மாத்திரைParser.உயிர்மெய்நெடில்Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_உயிர்மெய்நெடில்)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.மெய்()
            self.state = 71
            self.உயிர்நெடில்()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class உயிரளபெடைContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return மாத்திரைParser.RULE_உயிரளபெடை

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterஉயிரளபெடை" ):
                listener.enterஉயிரளபெடை(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitஉயிரளபெடை" ):
                listener.exitஉயிரளபெடை(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitஉயிரளபெடை" ):
                return visitor.visitஉயிரளபெடை(self)
            else:
                return visitor.visitChildren(self)




    def உயிரளபெடை(self):

        localctx = மாத்திரைParser.உயிரளபெடைContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_உயிரளபெடை)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << மாத்திரைParser.T__31) | (1 << மாத்திரைParser.T__32) | (1 << மாத்திரைParser.T__33) | (1 << மாத்திரைParser.T__34) | (1 << மாத்திரைParser.T__35) | (1 << மாத்திரைParser.T__36) | (1 << மாத்திரைParser.T__37))) != 0)):
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

    class ஒற்றளபெடைContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return மாத்திரைParser.RULE_ஒற்றளபெடை

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterஒற்றளபெடை" ):
                listener.enterஒற்றளபெடை(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitஒற்றளபெடை" ):
                listener.exitஒற்றளபெடை(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitஒற்றளபெடை" ):
                return visitor.visitஒற்றளபெடை(self)
            else:
                return visitor.visitChildren(self)




    def ஒற்றளபெடை(self):

        localctx = மாத்திரைParser.ஒற்றளபெடைContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ஒற்றளபெடை)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << மாத்திரைParser.T__18) | (1 << மாத்திரைParser.T__19) | (1 << மாத்திரைParser.T__20) | (1 << மாத்திரைParser.T__21) | (1 << மாத்திரைParser.T__22) | (1 << மாத்திரைParser.T__23) | (1 << மாத்திரைParser.T__24) | (1 << மாத்திரைParser.T__26) | (1 << மாத்திரைParser.T__27) | (1 << மாத்திரைParser.T__29) | (1 << மாத்திரைParser.T__30))) != 0)):
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





