def nod(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    print("НОД 12 и 18 =", nod(12, 18))