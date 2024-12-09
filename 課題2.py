students = [["田中", 85],["鈴木", 72],["佐藤", 90],["山田", 65],["中村", 88],]

# 80点以上の生徒の出力
print("【80点以上の学生】")
for student in students:
    if student[1] >= 80:
        print(f"{student[0]}:{student[1]}点")

# 平均点の出力

total_score = 0
count_student = 0
for student in students:
    total_score += student[1]
    count_student += 1
average = total_score/count_student
print("【クラスの平均点】")
print(f"{average}点")

#最高得点者の出力

highest = ["",0]
for studnt in students:
    if student[1] > highest[1]:
        highest = student
print("最高得点者")
print(f"{highest[0]}:{highest[1]}点")
for student in students:
    if student[1] == highest[1] and student[0] != highest[0]:
        print(f"{student[0]}:{student[1]}点")
        
#追試対象者の表示
print("【追試対象者】")
for student in students:
    if student[1] < 70:
        print(f"{student[0]}:{student[1]}点→追試必要")