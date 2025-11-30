def count_even_digits(n):
    n = abs(n)
    count = 0
    for digit in str(n):
        if int(digit) % 2 == 0:
            count += 1
    return count

# пример
if __name__ == "__main__":
    print(count_even_digits(123456))  # 3
