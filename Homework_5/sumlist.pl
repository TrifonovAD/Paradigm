sum_list([], 0).

sum_list([Head|Tail], Sum) :-
    sum_list(Tail, TailSum),
    Sum is Head + TailSum.


?- sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], Sum).
Sum = 55.

?- sum_list([-3, 2, 5], Sum).
Sum = 4.

?- sum_list([], Sum).
Sum = 0.