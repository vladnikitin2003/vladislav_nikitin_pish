def parse_csv(data):
    students = data.split(";")
    for student in students:
        if student.strip() == "":
            continue
        name, age, faculty = student.split(",")
        print(f"Имя: {name.strip()}, Возраст: {age.strip()}, Факультет: {faculty.strip()}")

if __name__ == "__main__":
    csv_data = "Иванов,20,Физика; Петров,21,Математика; Сидоров,19,Химия"
    parse_csv(csv_data)
