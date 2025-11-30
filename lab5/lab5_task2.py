import re

def extract_emails(text):
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return emails

if __name__ == "__main__":
    text = "Контакты: ivan@mail.com, petrov@gmail.com, info@company.ru"
    print(extract_emails(text))  # ['ivan@mail.com', 'petrov@gmail.com', 'info@company.ru']
