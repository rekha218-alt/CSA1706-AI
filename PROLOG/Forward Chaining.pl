% Forward Chaining

fact(fever).
fact(cough).

rule(fever, flu).
rule(cough, cold).

forward_chaining :-
    fact(Fact),
    rule(Fact, Conclusion),
    write(Fact),
    write(' -> '),
    write(Conclusion),
    nl,
    fail.

forward_chaining.
