grades = [5, 3, 4, 5, 2, 4, 3, 5, 5, 2, 4, 3, 5]

# 1. ����� ���������� ������ � ������
print("Total number of grades:", len(grades))

# 2. ������� ��� ����������� ������ ������
for grade in [2, 3, 4, 5]:
    count = grades.count(grade)
    print(f"Grade {grade}: {count} time")

# 3. ��������� ����� ������ [4, 5, 2]
grades.extend([4, 5, 2])
print("After adding new ratings:", grades)

# 4. ������� ������ ������ �� ������
grades.remove(2)
print("After removing the first deuce:", grades)

# 5. ������ � ������� �����������
sorted_grades = sorted(grades)
print("Ratings in ascending order:", sorted_grades)

# 6. ������ ������ 5 ������
first_five = grades[:5]
print("First 5 ratings:", first_five)

# 7. ������� ����
average = sum(grades) / len(grades)
print(f"Average score: {average:.2f}")

# 8. ����� ������ ������ � �������� �5�
only_fives = [grade for grade in grades if grade == 5]
print("Only A's:", only_fives)