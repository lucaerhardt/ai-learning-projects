students = [
    {"name": "Gerd", "hours_studied": 5, "score": 88},
    {"name": "Anna", "hours_studied": 3, "score": 75},
    {"name": "John", "hours_studied": 8, "score": 92}
]

for student in students:
    print(f"{student['name']} studied {student['hours_studied']} hours and scored {student['score']}")

def average_score(student_list):
    total = 0
    for s in student_list:
        total += s["score"]
    return total / len(student_list)

print("Average score:", average_score(students))
