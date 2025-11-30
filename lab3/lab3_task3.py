def is_palindrome(n):
    s = str(abs(n))
    return s == s[::-1]

# пример
if __name__ == "__main__":
    print(is_palindrome(12321))  # True
    print(is_palindrome(12345))  # False
