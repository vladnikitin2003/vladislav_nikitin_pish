def count_words(sentence):
    words = sentence.split()
    return len(words)

if __name__ == "__main__":
    sentence = "Это пример предложения для подсчета слов"
    print(count_words(sentence))  # 7
