# Generated from CQL.g4 by ANTLR 4.5.2
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\31j\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write(u"\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4")
        buf.write(u"\16\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write(u"\3\4\3\4\3\4\3\4\7\4+\n\4\f\4\16\4.\13\4\3\5\5\5\61\n")
        buf.write(u"\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6:\n\6\3\7\3\7\5\7>")
        buf.write(u"\n\7\3\b\3\b\3\b\3\b\3\t\3\t\5\tF\n\t\3\t\3\t\3\t\3\n")
        buf.write(u"\3\n\3\13\3\13\3\f\3\f\3\f\5\fR\n\f\3\r\5\rU\n\r\3\r")
        buf.write(u"\6\rX\n\r\r\r\16\rY\3\r\3\r\6\r^\n\r\r\r\16\r_\5\rb\n")
        buf.write(u"\r\3\16\3\16\3\17\3\17\3\20\3\20\3\20\2\3\6\21\2\4\6")
        buf.write(u"\b\n\f\16\20\22\24\26\30\32\34\36\2\5\3\2\b\r\3\2\23")
        buf.write(u"\24\3\2\25\27e\2 \3\2\2\2\4\"\3\2\2\2\6$\3\2\2\2\b\60")
        buf.write(u"\3\2\2\2\n9\3\2\2\2\f=\3\2\2\2\16?\3\2\2\2\20C\3\2\2")
        buf.write(u"\2\22J\3\2\2\2\24L\3\2\2\2\26Q\3\2\2\2\30T\3\2\2\2\32")
        buf.write(u"c\3\2\2\2\34e\3\2\2\2\36g\3\2\2\2 !\5\4\3\2!\3\3\2\2")
        buf.write(u"\2\"#\5\6\4\2#\5\3\2\2\2$%\b\4\1\2%&\5\b\5\2&,\3\2\2")
        buf.write(u"\2\'(\f\3\2\2()\7\20\2\2)+\5\b\5\2*\'\3\2\2\2+.\3\2\2")
        buf.write(u"\2,*\3\2\2\2,-\3\2\2\2-\7\3\2\2\2.,\3\2\2\2/\61\7\22")
        buf.write(u"\2\2\60/\3\2\2\2\60\61\3\2\2\2\61\62\3\2\2\2\62\63\5")
        buf.write(u"\n\6\2\63\t\3\2\2\2\64:\5\f\7\2\65\66\7\3\2\2\66\67\5")
        buf.write(u"\2\2\2\678\7\4\2\28:\3\2\2\29\64\3\2\2\29\65\3\2\2\2")
        buf.write(u":\13\3\2\2\2;>\5\16\b\2<>\5\20\t\2=;\3\2\2\2=<\3\2\2")
        buf.write(u"\2>\r\3\2\2\2?@\7\30\2\2@A\5\22\n\2AB\5\26\f\2B\17\3")
        buf.write(u"\2\2\2CE\7\30\2\2DF\7\22\2\2ED\3\2\2\2EF\3\2\2\2FG\3")
        buf.write(u"\2\2\2GH\5\24\13\2HI\5\36\20\2I\21\3\2\2\2JK\t\2\2\2")
        buf.write(u"K\23\3\2\2\2LM\t\3\2\2M\25\3\2\2\2NR\5\30\r\2OR\5\32")
        buf.write(u"\16\2PR\5\34\17\2QN\3\2\2\2QO\3\2\2\2QP\3\2\2\2R\27\3")
        buf.write(u"\2\2\2SU\7\6\2\2TS\3\2\2\2TU\3\2\2\2UW\3\2\2\2VX\7\16")
        buf.write(u"\2\2WV\3\2\2\2XY\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Za\3\2\2")
        buf.write(u"\2[]\7\7\2\2\\^\7\16\2\2]\\\3\2\2\2^_\3\2\2\2_]\3\2\2")
        buf.write(u"\2_`\3\2\2\2`b\3\2\2\2a[\3\2\2\2ab\3\2\2\2b\31\3\2\2")
        buf.write(u"\2cd\t\4\2\2d\33\3\2\2\2ef\7\17\2\2f\35\3\2\2\2gh\5\34")
        buf.write(u"\17\2h\37\3\2\2\2\f,\609=EQTY_a")
        return buf.getvalue()


class CQLParser ( Parser ):

    grammarFileName = "CQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'('", u"')'", u"'+'", u"'-'", u"'.'", 
                     u"'='", u"'<>'", u"'>'", u"'<'", u"'>='", u"'<='" ]

    symbolicNames = [ u"<INVALID>", u"LPAREN", u"RPAREN", u"PLUS", u"MINUS", 
                      u"PERIOD", u"EQ", u"NEQ", u"GT", u"LT", u"GTE", u"LTE", 
                      u"DIGIT", u"STRING", u"AND", u"OR", u"NOT", u"LIKE", 
                      u"ILIKE", u"TRUE", u"FALSE", u"UNKNOWN", u"ID", u"SPACE" ]

    RULE_search_condition = 0
    RULE_boolean_value_expression = 1
    RULE_boolean_term = 2
    RULE_boolean_factor = 3
    RULE_boolean_primary = 4
    RULE_predicate = 5
    RULE_comparison_predicate = 6
    RULE_text_predicate = 7
    RULE_comp_op = 8
    RULE_like_op = 9
    RULE_literal = 10
    RULE_numeric_literal = 11
    RULE_boolean_literal = 12
    RULE_character_string_literal = 13
    RULE_character_pattern = 14

    ruleNames =  [ u"search_condition", u"boolean_value_expression", u"boolean_term", 
                   u"boolean_factor", u"boolean_primary", u"predicate", 
                   u"comparison_predicate", u"text_predicate", u"comp_op", 
                   u"like_op", u"literal", u"numeric_literal", u"boolean_literal", 
                   u"character_string_literal", u"character_pattern" ]

    EOF = Token.EOF
    LPAREN=1
    RPAREN=2
    PLUS=3
    MINUS=4
    PERIOD=5
    EQ=6
    NEQ=7
    GT=8
    LT=9
    GTE=10
    LTE=11
    DIGIT=12
    STRING=13
    AND=14
    OR=15
    NOT=16
    LIKE=17
    ILIKE=18
    TRUE=19
    FALSE=20
    UNKNOWN=21
    ID=22
    SPACE=23

    def __init__(self, input):
        super(CQLParser, self).__init__(input)
        self.checkVersion("4.5.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Search_conditionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CQLParser.Search_conditionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def boolean_value_expression(self):
            return self.getTypedRuleContext(CQLParser.Boolean_value_expressionContext,0)


        def getRuleIndex(self):
            return CQLParser.RULE_search_condition

        def enterRule(self, listener):
            if hasattr(listener, "enterSearch_condition"):
                listener.enterSearch_condition(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSearch_condition"):
                listener.exitSearch_condition(self)




    def search_condition(self):

        localctx = CQLParser.Search_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_search_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.boolean_value_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Boolean_value_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CQLParser.Boolean_value_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def boolean_term(self):
            return self.getTypedRuleContext(CQLParser.Boolean_termContext,0)


        def getRuleIndex(self):
            return CQLParser.RULE_boolean_value_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterBoolean_value_expression"):
                listener.enterBoolean_value_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBoolean_value_expression"):
                listener.exitBoolean_value_expression(self)




    def boolean_value_expression(self):

        localctx = CQLParser.Boolean_value_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_boolean_value_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.boolean_term(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Boolean_termContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CQLParser.Boolean_termContext, self).__init__(parent, invokingState)
            self.parser = parser

        def boolean_factor(self):
            return self.getTypedRuleContext(CQLParser.Boolean_factorContext,0)


        def boolean_term(self):
            return self.getTypedRuleContext(CQLParser.Boolean_termContext,0)


        def AND(self):
            return self.getToken(CQLParser.AND, 0)

        def getRuleIndex(self):
            return CQLParser.RULE_boolean_term

        def enterRule(self, listener):
            if hasattr(listener, "enterBoolean_term"):
                listener.enterBoolean_term(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBoolean_term"):
                listener.exitBoolean_term(self)



    def boolean_term(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CQLParser.Boolean_termContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_boolean_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.boolean_factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 42
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CQLParser.Boolean_termContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_term)
                    self.state = 37
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 38
                    self.match(CQLParser.AND)
                    self.state = 39
                    self.boolean_factor() 
                self.state = 44
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Boolean_factorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CQLParser.Boolean_factorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def boolean_primary(self):
            return self.getTypedRuleContext(CQLParser.Boolean_primaryContext,0)


        def NOT(self):
            return self.getToken(CQLParser.NOT, 0)

        def getRuleIndex(self):
            return CQLParser.RULE_boolean_factor

        def enterRule(self, listener):
            if hasattr(listener, "enterBoolean_factor"):
                listener.enterBoolean_factor(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBoolean_factor"):
                listener.exitBoolean_factor(self)




    def boolean_factor(self):

        localctx = CQLParser.Boolean_factorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_boolean_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            _la = self._input.LA(1)
            if _la==CQLParser.NOT:
                self.state = 45
                self.match(CQLParser.NOT)


            self.state = 48
            self.boolean_primary()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Boolean_primaryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CQLParser.Boolean_primaryContext, self).__init__(parent, invokingState)
            self.parser = parser

        def predicate(self):
            return self.getTypedRuleContext(CQLParser.PredicateContext,0)


        def LPAREN(self):
            return self.getToken(CQLParser.LPAREN, 0)

        def search_condition(self):
            return self.getTypedRuleContext(CQLParser.Search_conditionContext,0)


        def RPAREN(self):
            return self.getToken(CQLParser.RPAREN, 0)

        def getRuleIndex(self):
            return CQLParser.RULE_boolean_primary

        def enterRule(self, listener):
            if hasattr(listener, "enterBoolean_primary"):
                listener.enterBoolean_primary(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBoolean_primary"):
                listener.exitBoolean_primary(self)




    def boolean_primary(self):

        localctx = CQLParser.Boolean_primaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_boolean_primary)
        try:
            self.state = 55
            token = self._input.LA(1)
            if token in [CQLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.predicate()

            elif token in [CQLParser.LPAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.match(CQLParser.LPAREN)
                self.state = 52
                self.search_condition()
                self.state = 53
                self.match(CQLParser.RPAREN)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PredicateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CQLParser.PredicateContext, self).__init__(parent, invokingState)
            self.parser = parser

        def comparison_predicate(self):
            return self.getTypedRuleContext(CQLParser.Comparison_predicateContext,0)


        def text_predicate(self):
            return self.getTypedRuleContext(CQLParser.Text_predicateContext,0)


        def getRuleIndex(self):
            return CQLParser.RULE_predicate

        def enterRule(self, listener):
            if hasattr(listener, "enterPredicate"):
                listener.enterPredicate(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPredicate"):
                listener.exitPredicate(self)




    def predicate(self):

        localctx = CQLParser.PredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_predicate)
        try:
            self.state = 59
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.comparison_predicate()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.text_predicate()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Comparison_predicateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CQLParser.Comparison_predicateContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CQLParser.ID, 0)

        def comp_op(self):
            return self.getTypedRuleContext(CQLParser.Comp_opContext,0)


        def literal(self):
            return self.getTypedRuleContext(CQLParser.LiteralContext,0)


        def getRuleIndex(self):
            return CQLParser.RULE_comparison_predicate

        def enterRule(self, listener):
            if hasattr(listener, "enterComparison_predicate"):
                listener.enterComparison_predicate(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitComparison_predicate"):
                listener.exitComparison_predicate(self)




    def comparison_predicate(self):

        localctx = CQLParser.Comparison_predicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_comparison_predicate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(CQLParser.ID)
            self.state = 62
            self.comp_op()
            self.state = 63
            self.literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Text_predicateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CQLParser.Text_predicateContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CQLParser.ID, 0)

        def like_op(self):
            return self.getTypedRuleContext(CQLParser.Like_opContext,0)


        def character_pattern(self):
            return self.getTypedRuleContext(CQLParser.Character_patternContext,0)


        def NOT(self):
            return self.getToken(CQLParser.NOT, 0)

        def getRuleIndex(self):
            return CQLParser.RULE_text_predicate

        def enterRule(self, listener):
            if hasattr(listener, "enterText_predicate"):
                listener.enterText_predicate(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitText_predicate"):
                listener.exitText_predicate(self)




    def text_predicate(self):

        localctx = CQLParser.Text_predicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_text_predicate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(CQLParser.ID)
            self.state = 67
            _la = self._input.LA(1)
            if _la==CQLParser.NOT:
                self.state = 66
                self.match(CQLParser.NOT)


            self.state = 69
            self.like_op()
            self.state = 70
            self.character_pattern()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Comp_opContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CQLParser.Comp_opContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(CQLParser.EQ, 0)

        def NEQ(self):
            return self.getToken(CQLParser.NEQ, 0)

        def GT(self):
            return self.getToken(CQLParser.GT, 0)

        def LT(self):
            return self.getToken(CQLParser.LT, 0)

        def GTE(self):
            return self.getToken(CQLParser.GTE, 0)

        def LTE(self):
            return self.getToken(CQLParser.LTE, 0)

        def getRuleIndex(self):
            return CQLParser.RULE_comp_op

        def enterRule(self, listener):
            if hasattr(listener, "enterComp_op"):
                listener.enterComp_op(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitComp_op"):
                listener.exitComp_op(self)




    def comp_op(self):

        localctx = CQLParser.Comp_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comp_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CQLParser.EQ) | (1 << CQLParser.NEQ) | (1 << CQLParser.GT) | (1 << CQLParser.LT) | (1 << CQLParser.GTE) | (1 << CQLParser.LTE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Like_opContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CQLParser.Like_opContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LIKE(self):
            return self.getToken(CQLParser.LIKE, 0)

        def ILIKE(self):
            return self.getToken(CQLParser.ILIKE, 0)

        def getRuleIndex(self):
            return CQLParser.RULE_like_op

        def enterRule(self, listener):
            if hasattr(listener, "enterLike_op"):
                listener.enterLike_op(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLike_op"):
                listener.exitLike_op(self)




    def like_op(self):

        localctx = CQLParser.Like_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_like_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            _la = self._input.LA(1)
            if not(_la==CQLParser.LIKE or _la==CQLParser.ILIKE):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CQLParser.LiteralContext, self).__init__(parent, invokingState)
            self.parser = parser

        def numeric_literal(self):
            return self.getTypedRuleContext(CQLParser.Numeric_literalContext,0)


        def boolean_literal(self):
            return self.getTypedRuleContext(CQLParser.Boolean_literalContext,0)


        def character_string_literal(self):
            return self.getTypedRuleContext(CQLParser.Character_string_literalContext,0)


        def getRuleIndex(self):
            return CQLParser.RULE_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterLiteral"):
                listener.enterLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteral"):
                listener.exitLiteral(self)




    def literal(self):

        localctx = CQLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_literal)
        try:
            self.state = 79
            token = self._input.LA(1)
            if token in [CQLParser.MINUS, CQLParser.DIGIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.numeric_literal()

            elif token in [CQLParser.TRUE, CQLParser.FALSE, CQLParser.UNKNOWN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.boolean_literal()

            elif token in [CQLParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 78
                self.character_string_literal()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Numeric_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CQLParser.Numeric_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(CQLParser.MINUS, 0)

        def DIGIT(self, i=None):
            if i is None:
                return self.getTokens(CQLParser.DIGIT)
            else:
                return self.getToken(CQLParser.DIGIT, i)

        def PERIOD(self):
            return self.getToken(CQLParser.PERIOD, 0)

        def getRuleIndex(self):
            return CQLParser.RULE_numeric_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterNumeric_literal"):
                listener.enterNumeric_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNumeric_literal"):
                listener.exitNumeric_literal(self)




    def numeric_literal(self):

        localctx = CQLParser.Numeric_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_numeric_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            _la = self._input.LA(1)
            if _la==CQLParser.MINUS:
                self.state = 81
                self.match(CQLParser.MINUS)


            self.state = 85 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 84
                    self.match(CQLParser.DIGIT)

                else:
                    raise NoViableAltException(self)
                self.state = 87 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 95
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 89
                self.match(CQLParser.PERIOD)
                self.state = 91 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 90
                        self.match(CQLParser.DIGIT)

                    else:
                        raise NoViableAltException(self)
                    self.state = 93 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Boolean_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CQLParser.Boolean_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(CQLParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(CQLParser.FALSE, 0)

        def UNKNOWN(self):
            return self.getToken(CQLParser.UNKNOWN, 0)

        def getRuleIndex(self):
            return CQLParser.RULE_boolean_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterBoolean_literal"):
                listener.enterBoolean_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBoolean_literal"):
                listener.exitBoolean_literal(self)




    def boolean_literal(self):

        localctx = CQLParser.Boolean_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_boolean_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CQLParser.TRUE) | (1 << CQLParser.FALSE) | (1 << CQLParser.UNKNOWN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Character_string_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CQLParser.Character_string_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CQLParser.STRING, 0)

        def getRuleIndex(self):
            return CQLParser.RULE_character_string_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterCharacter_string_literal"):
                listener.enterCharacter_string_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCharacter_string_literal"):
                listener.exitCharacter_string_literal(self)




    def character_string_literal(self):

        localctx = CQLParser.Character_string_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_character_string_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(CQLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Character_patternContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CQLParser.Character_patternContext, self).__init__(parent, invokingState)
            self.parser = parser

        def character_string_literal(self):
            return self.getTypedRuleContext(CQLParser.Character_string_literalContext,0)


        def getRuleIndex(self):
            return CQLParser.RULE_character_pattern

        def enterRule(self, listener):
            if hasattr(listener, "enterCharacter_pattern"):
                listener.enterCharacter_pattern(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCharacter_pattern"):
                listener.exitCharacter_pattern(self)




    def character_pattern(self):

        localctx = CQLParser.Character_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_character_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.character_string_literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.boolean_term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def boolean_term_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




