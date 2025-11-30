def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

if __name__ == "__main__":
    string = "abracadabra"
    print(char_frequency(string))  # {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
