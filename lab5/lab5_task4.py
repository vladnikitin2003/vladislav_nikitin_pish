def remove_consecutive_duplicates(s):
    if not s:
        return ""
    result = [s[0]]
    for char in s[1:]:
        if char != result[-1]:
            result.append(char)
    return "".join(result)

if __name__ == "__main__":
    text = "aaabbcddddeeeffg"
    print(remove_consecutive_duplicates(text))  # 'abcdefg'
