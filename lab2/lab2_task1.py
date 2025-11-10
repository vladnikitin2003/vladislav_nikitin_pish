def f(x):
    if -2 <= x < 2:
        return x**2
    elif x >= 2:
        return x**2 + 4*x + 5
    else:  # x < -2
        return 4
    
if __name__ == "__main__":
    for x in [-3, 0, 3]:
        print(f"f({x}) = {f(x)}")