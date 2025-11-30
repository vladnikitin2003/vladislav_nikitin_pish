def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_strong_number(n):
    total = 0
    for digit in str(abs(n)):
        total += factorial(int(digit))
    return total == n

# пример
if __name__ == "__main__":
    print(is_strong_number(145))  # True
    print(is_strong_number(123))  # False
