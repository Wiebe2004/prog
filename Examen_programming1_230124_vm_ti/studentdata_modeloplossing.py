def calculate_average(grades):
    dict_avg = {}
    for name in grades:
        s = sum(grades[name])
        c = len(grades[name])
        dict_avg[name] = round(s/c,1)
    return dict_avg

def calculate_stats(input):
    with open(input) as infile:
        doc = infile.readlines()
    by_course = {}
    by_student = {}
    for line in doc:
        name, course, grade = line.split(",")
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

    with open('results.txt','w') as outfile:
        outfile.write("Per course: \n")
        for course in by_course_avg:
            outfile.write(f"\t{course}: {by_course_avg[course]}\n")
        outfile.write("Per student: \n")
        for student in by_student_avg:
            outfile.write(f"\t{student}: {by_student_avg[student]}\n")

calculate_stats('studentdata.txt')
        

    