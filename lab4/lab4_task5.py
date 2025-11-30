def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

if __name__ == "__main__":
    string1 = "listen"
    string2 = "silent"
    print(is_anagram(string1, string2))  # True
