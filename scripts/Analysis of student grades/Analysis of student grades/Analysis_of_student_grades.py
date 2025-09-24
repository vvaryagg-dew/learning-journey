grades = [5, 3, 4, 5, 2, 4, 3, 5, 5, 2, 4, 3, 5]

# 1. Общее количество оценок в списке
print("Total number of grades:", len(grades))

# 2. Сколько раз встречается каждая оценка
for grade in [2, 3, 4, 5]:
    count = grades.count(grade)
    print(f"Grade {grade}: {count} time")

# 3. Добавляем новые оценки [4, 5, 2]
grades.extend([4, 5, 2])
print("After adding new ratings:", grades)

# 4. Удаляем первую двойку из списка
grades.remove(2)
print("After removing the first deuce:", grades)

# 5. Оценки в порядке возрастания
sorted_grades = sorted(grades)
print("Ratings in ascending order:", sorted_grades)

# 6. Только первые 5 оценок
first_five = grades[:5]
print("First 5 ratings:", first_five)

# 7. Средний балл
average = sum(grades) / len(grades)
print(f"Average score: {average:.2f}")

# 8. Новый список только с оценками «5»
only_fives = [grade for grade in grades if grade == 5]
print("Only A's:", only_fives)