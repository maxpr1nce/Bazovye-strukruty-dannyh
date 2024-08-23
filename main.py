def calculate_average_grades(grades, students):
    # Создаем словарь для хранения средних баллов
    average_grades = {}

    # Проходим по множеству студентов
    for student in students:
        # Находим индекс студента в списке grades
        student_index = sorted(students).index(student)

        # Вычисляем средний балл студента
        student_grades = grades[student_index]
        average_grade = sum(student_grades) / len(student_grades)

        # Добавляем студента и его средний балл в словарь
        average_grades[student] = average_grade

    return average_grades

# Пример использования
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

result = calculate_average_grades(grades, students)
print(result)
