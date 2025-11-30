def unique_words(sentence):
    words = sentence.split()
    unique = sorted(set(words))
    return unique

if __name__ == "__main__":
    sentence = "apple banana apple orange banana kiwi"
    print(unique_words(sentence))  # ['apple', 'banana', 'kiwi', 'orange']

