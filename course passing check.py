grades = []

n = int(input("how many students?: "))
for _ in range(n):
    name = input("name of the student: ")
    grade = float(input("grade: "))

    grades.append((name, grade))

passed = [x for x in grades if x[1] >= 50]

print(f"passed: {passed}")