import re

def extract_numbers(s):
    numbers = re.findall(r'\d+', s)
    return [int(num) for num in numbers]

if __name__ == "__main__":
    text = "У меня 2 яблока и 15 апельсинов, всего 17 фруктов."
    print(extract_numbers(text))  # [2, 15, 17]
