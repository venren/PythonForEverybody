import numpy as np
def bestAvgGrade(grades: dict):
    store = {}
    for student, grade in grades:
        if student not in store:
            store[student] = np.array([])
        store[student].append(grade)

    for student, marks in store:
        store[student] = np.average(marks)

    return store

print(bestAvgGrade({"John": 90, "Jane": 80, "John": 85, "Jane": 95}))