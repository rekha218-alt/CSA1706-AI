% Diet Recommendation System

diet(diabetes, 'Low sugar diet').
diet(hypertension, 'Low salt diet').
diet(obesity, 'Low calorie diet').
diet(anemia, 'Iron rich diet').
diet(fever, 'Light and nutritious food').

% Rule

suggest_diet(Disease, Diet) :-
    diet(Disease, Diet).
