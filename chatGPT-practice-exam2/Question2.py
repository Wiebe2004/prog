def calculate_avg(by_salary):
    # dict_avg = {}
    s = 0
    c = 0
    for name in by_salary:
        s += sum(by_salary[name])
        c += 1
    return round(s / c, 1)


def em_p_department(by_department):
    dict_per_dep = {}
    for department in by_department:
        dict_per_dep[department] = len(by_department[department])
    return dict_per_dep

def highest_paid(by_salary):
    lijst = []
    hoogste = max(by_salary.values())
    for name,salary in by_salary.items():
        if salary == hoogste:
            lijst.append(name)
            hoogste = salary
    return str(lijst)

def process_employee_records(input_file, output_file):
    with open(input_file, "r") as file:
        doc = file.readlines()

    by_salary = {}
    by_department = {}

    for line in doc:
        EmployeeID, Name, Department, Salary = line.split(", ")
        Salary = int(Salary)
        if Name not in by_salary:
            by_salary[Name] = [Salary]
        else:
            by_salary[Name].append(Salary)

        if Department not in by_department:
            by_department[Department] = [Name]
        else:
            by_department[Department].append(Name)

    by_avg_salary = calculate_avg(by_salary)
    highest_paid_empl = highest_paid(by_salary)
    by_empl_p_dep = em_p_department(by_department)

    with open(output_file, "w", encoding="utf-8") as outFile:
        outFile.write(f"Average salary: {by_avg_salary}\n")
        outFile.write(f"Highest paid: {highest_paid_empl}\n")
        outFile.write(f"Employees per Department\n")
        for dep,empl in by_empl_p_dep.items():
            outFile.write(f"\t{dep}: {empl}\n")


process_employee_records("employees.txt", "summary.txt")
