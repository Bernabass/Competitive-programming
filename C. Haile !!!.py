n = int(input())
for i in range(n):
    student = input()
    student = student.split("#")
    student = " ".join(student)
    print(student)