#task 1

def calculate_product(list):
    product = 1
    for num in list:
        product *= num
    return product

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = calculate_product(numbers)
print(f"Součin všech čísel v seznamu je: {result}")


#task 2
def minimum(list):
    minimum = list[0]
    for num in list[1:]:
        if num < minimum:
            minimum = num
    return minimum


numbers = [8, 15, 2, 8, 10, 42, 65]
result = minimum(numbers)
print(f"Minimální hodnota čísla z listu je: {result}")