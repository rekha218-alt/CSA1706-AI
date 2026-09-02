% Student - Teacher - Subject Code Database

student_teacher_subject(rahul, kumar, cs101).
student_teacher_subject(priya, anitha, cs102).
student_teacher_subject(arun, kumar, cs103).
student_teacher_subject(sneha, anitha, cs104).

% Find teacher and subject using student

find_student(Student, Teacher, Subject) :-
    student_teacher_subject(Student, Teacher, Subject).

% Find students using teacher

find_teacher(Teacher, Student, Subject) :-
    student_teacher_subject(Student, Teacher, Subject).

% Find student and teacher using subject code

find_subject(Subject, Student, Teacher) :-
    student_teacher_subject(Student, Teacher, Subject).
