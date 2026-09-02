% Backward Chaining

fact(fever).
fact(cough).

rule(flu, fever).
rule(flu, cough).

% Backward chaining

prove(Goal) :-
    fact(Goal).

prove(Goal) :-
    rule(Goal, Condition1),
    prove(Condition1),
    rule(Goal, Condition2),
    prove(Condition2).
