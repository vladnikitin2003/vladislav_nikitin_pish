def prod(lst):
    result = 1
    for x in lst:
        result *= x
    return result

def sum_eq_product(n):
    digits = [int(d) for d in str(abs(n))]
    return sum(digits) == prod(digits)

if __name__ == "__main__":
    test_numbers = [123, 22, 1124]
    for num in test_numbers:
        print(f"{num}: сумма цифр = произведению цифр? {sum_eq_product(num)}")