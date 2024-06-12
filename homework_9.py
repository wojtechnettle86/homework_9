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


#task 3
def prime_num(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
    #toto mám z chatgpt

def count_primes(int_list):
    prime_count = 0
    for number in int_list:
        if prime_num(number):
            prime_count += 1
    return prime_count

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 17]
result = count_primes(numbers)
print(f"Počet prvočísel v seznamu je: {result}")


#task 4
def remove(list, num_remove):
    original_length = len(list)
    list[:] = [num for num in list if num != num_remove]
    removed_count = original_length - len(list)
    return removed_count


numbers = [1, 2, 3, 4, 2, 5, 2, 6, 7, 2]
num_to_remove = 6
removed_elements_count = remove(numbers, num_to_remove)
print(f"Počet odstraněných čísel: {removed_elements_count}")
print(f"Seznam po odstranění: {numbers}")