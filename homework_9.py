#task 1

def calculate_product(list):
    product = 1
    for num in list:
        product *= num
    return product

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = calculate_product(numbers)
print(f"Součin všech čísel v seznamu je: {result}")