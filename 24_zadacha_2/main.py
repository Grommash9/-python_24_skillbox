import random
from student import StudentClass

names_list = []
is_done = False

with open('names.txt', 'r') as names_file:
    for line in names_file:
        if line.endswith('\n'):
            line = line[:-1]
        names_list.append(line)

student_list = [StudentClass(name, random.randint(0, 444), [x + random.randint(0, 99) for x in (1, 1, 1, 1, 1)])
                for name in names_list]

while not is_done:
    counter = 0
    for student_index in range(len(student_list) - 1):
        if student_list[student_index].average_score > student_list[student_index + 1].average_score:
            student_list[student_index].average_score, student_list[student_index + 1].average_score = \
                student_list[student_index + 1].average_score, student_list[student_index].average_score
            counter += 1
    if counter == 0:
        is_done = True

with open('result.txt', 'w') as results_file:
    for students in student_list:
        print(students.info())
        results_file.write(students.info())
        results_file.write('\n')
