% Medical Diagnosis System

symptom(ravi, fever).
symptom(ravi, cough).

symptom(priya, fever).
symptom(priya, rash).

symptom(arun, cough).
symptom(arun, breathlessness).

% Diagnosis rules

diagnosis(Patient, flu) :-
    symptom(Patient, fever),
    symptom(Patient, cough).

diagnosis(Patient, measles) :-
    symptom(Patient, fever),
    symptom(Patient, rash).

diagnosis(Patient, pneumonia) :-
    symptom(Patient, cough),
    symptom(Patient, breathlessness).
