% Best First Search

edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(c, g).

% Heuristic values

h(a, 5).
h(b, 4).
h(c, 3).
h(d, 1).
h(e, 2).
h(f, 1).
h(g, 0).

best_first(Start, Goal, Path) :-
    search([[Start]], Goal, Path).

search([[Goal|Path]|_], Goal, Result) :-
    reverse([Goal|Path], Result).

search([[Current|Path]|Rest], Goal, Result) :-
    findall(
        [Next,Current|Path],
        (
            edge(Current, Next),
            \+ member(Next, [Current|Path])
        ),
        Children
    ),
    add_to_queue(Children, Rest, NewQueue),
    sort_queue(NewQueue, SortedQueue),
    search(SortedQueue, Goal, Result).

add_to_queue([], Queue, Queue).

add_to_queue([H|T], Queue, NewQueue) :-
    append(Queue, [H], Temp),
    add_to_queue(T, Temp, NewQueue).

sort_queue(Queue, Sorted) :-
    predsort(compare_paths, Queue, Sorted).

compare_paths(Order, [A|_], [B|_]) :-
    h(A, HA),
    h(B, HB),
    compare(Order, HA, HB).
