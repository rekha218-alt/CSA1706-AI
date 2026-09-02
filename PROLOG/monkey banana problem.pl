% Monkey Banana Problem

% State:
% state(MonkeyPosition, BoxPosition, MonkeyHeight, BananaPosition)

can_get_banana(
    state(Monkey, Box, floor, Banana),
    state(Monkey, Box, standing, Banana)
) :-
    Monkey = Box.

can_get_banana(
    state(Monkey, Box, floor, Banana),
    state(Box, Box, floor, Banana)
) :-
    Monkey \= Box.

can_get_banana(
    state(Box, Box, floor, Banana),
    state(Box, Box, standing, Banana)
).

can_get_banana(
    state(Box, Box, standing, Banana),
    state(Box, Box, standing, Banana)
) :-
    Box = Banana.
