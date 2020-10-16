# put your python code here
class_1_students = int(input())
class_2_students = int(input())
class_3_students = int(input())
classes = [class_1_students, class_2_students, class_3_students]

total_desks = 0
for students in classes:
    total_desks += (students // 2) + students % 2

print(total_desks)
