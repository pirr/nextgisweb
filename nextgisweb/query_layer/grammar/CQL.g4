grammar CQL;

search_condition
    : boolean_value_expression
    ;

boolean_value_expression
    : boolean_term
    //| boolean_value_expression OR boolean_term
    ;

boolean_term
    : boolean_factor
    | boolean_term AND boolean_factor
    ;

boolean_factor
    : NOT? boolean_primary
    ;

boolean_primary
    : predicate
    | LPAREN search_condition RPAREN
    ;

predicate
    : comparison_predicate
    | text_predicate
    ;

comparison_predicate
    : ID comp_op literal
    ;

text_predicate
    : ID NOT? like_op character_pattern
    ;

comp_op
    : EQ
    | NEQ
    | GT
    | LT
    | GTE
    | LTE
    ;

like_op
    : LIKE
    | ILIKE
    ;

literal
    : numeric_literal
    | boolean_literal
    | character_string_literal
    ;

numeric_literal
    : MINUS? DIGIT+ (PERIOD DIGIT+)?
    ;

boolean_literal
    : TRUE
    | FALSE
    | UNKNOWN
    ;

character_string_literal
    : STRING
    ;

character_pattern
    : character_string_literal
    ;


LPAREN:     '(';
RPAREN:     ')';
PLUS:       '+';
MINUS:      '-';
PERIOD:     '.';
EQ:         '=';
NEQ:        '<>';
GT:         '>';
LT:         '<';
GTE:        '>=';
LTE:        '<=';
DIGIT:      [0-9];
STRING:     '\'' (~'\'' | '\'\'')* '\'';

AND:        A N D;
OR:         O R;
NOT:        N O T;
LIKE:       L I K E;
ILIKE:      I L I K E;
TRUE:       T R U E;
FALSE:      F A L S E;
UNKNOWN:    U N K N O W N;

ID:         [a-zA-Z]+;
SPACE:      [ \t\r\n]+ -> skip;

fragment A:     [aA];
fragment B:     [bB];
fragment C:     [cC];
fragment D:     [dD];
fragment E:     [eE];
fragment F:     [fF];
fragment G:     [gG];
fragment H:     [hH];
fragment I:     [iI];
fragment J:     [jJ];
fragment K:     [kK];
fragment L:     [lL];
fragment M:     [mM];
fragment N:     [nN];
fragment O:     [oO];
fragment P:     [pP];
fragment Q:     [qQ];
fragment R:     [rR];
fragment S:     [sS];
fragment T:     [tT];
fragment U:     [uU];
fragment V:     [vV];
fragment W:     [wW];
fragment X:     [xX];
fragment Y:     [yY];
fragment Z:     [zZ];
