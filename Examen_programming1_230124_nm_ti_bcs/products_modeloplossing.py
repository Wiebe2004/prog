import math

def calculate_average(products):
    s = 0
    c = 0
    for price in products.values():
        s += price
        c += 1
    return round(s/c,0)

def most_expensive(products):
    duurste = -1
    lijst = []
    for name, price in products.items():
        price = int(price)
        if price == duurste:
            lijst.append(name)
        elif price > duurste:
            duurste = price
            lijst = [name]
    return lijst

def calculate_stats(input):
    with open(input) as infile:
        doc = infile.readlines()
    dict = {}
    for line in doc:
        name,price = line.split(",")
        dict[name] = int(price)

    exp = most_expensive(dict)
    avg = calculate_average(dict)

    with open('results.txt','w') as outfile:
        outfile.write(f"Total number of products: {len(dict)}\n")
        outfile.write(f"Average price: {avg}\n")
        outfile.write(f"Most expensive products:\n")
        for p in exp:
            outfile.write(f"\t{p}\n")



calculate_stats('products.txt')
