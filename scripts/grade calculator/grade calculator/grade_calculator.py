# Список с оценками студентов
grades = [5, 3, 4, 5, 2, 4, 3, 5, 5, 2, 4, 3, 5]

# Функция для расчета среднего балла
def average_grade(grades):
    return round(sum(grades) / len(grades), 2)

# Функция для подсчета количества определенной оценки
def count_grade(grades, grade):
    count = 0
    for g in grades:
        if g == grade:
            count += 1
    return count

# Функция для получения всех оценок "5"
def best_students(grades):
    best = []
    for grade in grades:
        if grade == 5:
            best.append(grade)
    return best

# Основная программа
print("Average grade:", average_grade(grades))
print("Count of grade 5:", count_grade(grades, 5))
print("Best students grades:", best_students(grades))
