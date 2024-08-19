def process_employee_records(input, output):
    highest_salary = 0
    highest_paid_employee = ''
    department_counts = {}
    with open(input, 'r') as input_file:
        with open(output, 'w') as output_file:
            name_list = []
            salary_list = []

            for line in input_file:
                employee_id, name, department, salary = line.strip().split(', ')
                salary = int(salary)

                name_list.append(name)
                salary_list.append(salary)

                if salary > highest_salary:
                    highest_salary = salary
                    highest_paid_employee = name

                if department not in department_counts:
                    department_counts[department] = 1
                else:
                    department_counts[department] += 1

            avg_salary = sum(salary_list) / len(name_list)

            output_file.write(f'Average Salary: {avg_salary}\n')
            output_file.write(f'Highest Paid: {highest_paid_employee}\n')
            output_file.write(f'Employees per Department:\n')
            for department, count in department_counts.items():
                output_file.write(f'- {department}: {count}\n')

            


process_employee_records('employees.txt', 'summary.txt')