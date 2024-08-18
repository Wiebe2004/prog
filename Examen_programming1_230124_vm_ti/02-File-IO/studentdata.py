
def calculate_average(grades):
    result = {}
    for name in grades:
        s = sum(grades[name])
        c = len(grades[name])
        result[name] = round(s/c,1)  #The 1 in the round(s/c, 1) function specifies that the result should be rounded to one decimal place.
    return result

def calculate_stats(input):
    with open(input) as file:
        doc = file.readlines()
    by_course = {}
    by_student = {}
    for line in doc:
        name,course,grade = line.split(',')
        grade = int(grade)
        if course not in by_course:
            by_course[course] = [grade]
        else:
            by_course[course].append(grade)
        if name not in by_student:
            by_student[name] = [grade]
        else:
            by_student[name].append(grade)

    by_course_avg = calculate_average(by_course)
    by_student_avg = calculate_average(by_student)
    
    with open("results.txt", 'w',encoding='utf-8') as out_file:
        out_file.write("Per course: \n")
        for course in by_course_avg:
            out_file.write(f'\t{course}: {by_course_avg[course]}\n')
        out_file.write("Per student: \n")
        for student in by_student_avg:
            out_file.write(f'\t{student}: {by_student_avg[student]}\n')

calculate_stats('studentdata.txt')

# import os
# print(os.getcwd())
