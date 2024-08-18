def total_sales_by_product(sales):
    total_sold = {}
    for p_name, q_sales in sales.items():
        total_sold[p_name] = sum(q_sales)
    return total_sold


test_sales = {"Laptop": [5, 3], "Smartphone": [8, 7], "Camera": [4], "Tablet": [6]}

print(total_sales_by_product(test_sales))

total_sales = {"Laptop": 8, "Smartphone": 15, "Camera": 4, "Tablet": 6}


def best_selling_product(sales):
    lijst = []
    hoogste = max(sales.values())
    for p_name, q_sales in sales.items():
        if hoogste == q_sales:
            lijst.append(p_name)
    return lijst


print(best_selling_product(total_sales))


def calculate_sales_stats(input):
    with open(input) as file:
        doc = file.readlines()

    sales = {}

    for line in doc:
        date, p_name, s_quantity = line.split(", ")
        s_quantity = int(s_quantity)
        if p_name not in sales: #Altijd in haakjes!!!!
            sales[p_name] = [s_quantity]
        else:
            sales[p_name].append(s_quantity)

    total_sales = total_sales_by_product(sales)
    best_selling = best_selling_product(total_sales)

    with open("sales_results.txt", 'w', encoding='utf-8') as outFile:
        outFile.write(f"Total number of products: {len(total_sales)}\n")
        outFile.write(f"Best elling product(s):\n")
        for p in best_selling:
            outFile.write(f"\t{p}\n")


print(calculate_sales_stats('sales.txt'))