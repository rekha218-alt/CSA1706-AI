% Bird Database

bird(parrot).
bird(eagle).
bird(pigeon).
bird(hen).
bird(penguin).

can_fly(parrot).
can_fly(eagle).
can_fly(pigeon).

cannot_fly(hen).
cannot_fly(penguin).

% Rule

flies(Bird) :-
    can_fly(Bird).

does_not_fly(Bird) :-
    cannot_fly(Bird).
