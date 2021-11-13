import csv
from functools import reduce


def get_final_grades(filename='grades.csv'):
    weights = [0.2, 0.25, 0.25, 0.3]
    with open(filename) as file:
        # Almost unreadable but pythonic one line code of calculating the students grades
        students_grades = {r[0]: reduce(lambda a, b: a+b, [float(r[i+1]) * weights[i] if float(
            r[i+1]) != -1 else 0 for i in range(4)]) for r in csv.reader(file)}
    return students_grades
