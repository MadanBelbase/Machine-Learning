CREATE TABLE student_performance (
    id INTEGER PRIMARY KEY,
    hours_studied INTEGER,
    attendance_percentage INTEGER,
    previous_score INTEGER,
    sleep_hours INTEGER,
    internet_access INTEGER,
    final_score INTEGER
);

INSERT INTO student_performance 
(id, hours_studied, attendance_percentage, previous_score, sleep_hours, internet_access, final_score)
VALUES
(1, 2, 65, 50, 6, 1, 55),
(2, 4, 72, 60, 7, 1, 65),
(3, 1, 55, 45, 5, 0, 48),
(4, 6, 85, 75, 8, 1, 82),
(5, 3, 70, 58, 6, 0, 60),
(6, 8, 92, 88, 8, 1, 90),
(7, 5, 78, 68, 7, 1, 72),
(8, 0, 40, 35, 4, 0, 38);
