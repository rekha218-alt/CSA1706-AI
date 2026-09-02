% Family Tree

parent(john, mary).
parent(john, david).
parent(susan, mary).
parent(susan, david).

parent(david, peter).
parent(david, lisa).

male(john).
male(david).
male(peter).

female(susan).
female(mary).
female(lisa).

% Rules

father(X, Y) :-
    male(X),
    parent(X, Y).

mother(X, Y) :-
    female(X),
    parent(X, Y).

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.
