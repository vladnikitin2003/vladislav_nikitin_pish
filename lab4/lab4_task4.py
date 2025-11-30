def squares_dict(n):
    return {i: i**2 for i in range(1, n+1)}

if __name__ == "__main__":
    n = 5
    print(squares_dict(n))  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
