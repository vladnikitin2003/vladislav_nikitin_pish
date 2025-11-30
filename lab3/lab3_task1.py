def product_of_digits(n):
    n = abs(n)
    result = 1
    for digit in str(n):
        result *= int(digit)
    return result

# пример
if __name__ == "__main__":
    print(product_of_digits(1234))  # 24
