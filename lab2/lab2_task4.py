def sum_digits(n):
    return sum(int(d) for d in str(abs(n)))

if __name__ == "__main__":
    test_numbers = [123, -456, 7890]
    for num in test_numbers:
        print(f"Сумма цифр {num} = {sum_digits(num)}")
