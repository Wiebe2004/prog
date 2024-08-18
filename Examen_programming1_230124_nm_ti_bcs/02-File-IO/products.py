def calculate_average(products):
    s = 0
    c = 0
    for price in products:
        s += products[price]
        c += 1
    return round(s/c,0) 

# def most_expensive(products):
#     result = []
#     duurste = -1 
#     for name, price in products.items():
#         price = int(price)
#         if price == duurste:
#             result.append(name)
#         elif price > duurste:
#             duurste = price
#             result = [name]
#     return result

def most_expensive(products):
    result = []
    duurste = max(products.values()) 
    for name, price in products.items():
        # price = int(price)
        if price == duurste:
            result.append(name)
    return result

def calculate_stats(input):
    with open(input) as input:
        doc = input.readlines()

    dict = {}
    for line in doc:
        name,price = line.split(',')
        dict[name] = int(price)

    exp = most_expensive(dict)
    avg = calculate_average(dict)
        
    with open('results-new.txt', 'w',encoding="utf-8") as outFile:
        outFile.write(f"Total numbr of products: {len(doc)}\n")
        outFile.write(f"Average price: {avg}\n")
        outFile.write(f"Most expensive products:\n")
        for p in exp:
            outFile.write(f"\t{p}\n")

calculate_stats("products.txt")
    