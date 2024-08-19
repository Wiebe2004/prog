def analyze_grades(grades):
    grades1 = []
    result = {}
    highest_grade_name = []
    highest_grade = 0
    grade_distribution = {}

    for name, grade in grades:    
        grades1.append(grade)
        if grade > grades1[0]:
            highest_grade = grade
            highest_grade_name.append(name)
        
        if grade not in grade_distribution:
            grade_distribution[grade] = [name]
        else:
            grade_distribution[grade].append(name)

    average = sum(grades1) / len(grades1)


    result['average'] = average
    result['highest'] = highest_grade_name
    result['grade_distribution'] = grade_distribution
    return result

grades = [("Alice", 85), ("Bob", 90), ("Charlie", 78), ("Diana", 90)]
result = analyze_grades(grades)
print(result['average'])  
print(result['highest'])
print(result['grade_distribution']) 