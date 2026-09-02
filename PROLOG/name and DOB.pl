% Name and DOB Database

person(rahul, '10-05-2004').
person(priya, '15-08-2003').
person(arun, '20-01-2005').
person(sneha, '25-12-2004').

get_dob(Name, DOB) :-
    person(Name, DOB).

get_name(DOB, Name) :-
    person(Name, DOB).
