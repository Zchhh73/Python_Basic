import sys

score = int(sys.argv[1])

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print('Grade=' + grade)

result = '及格' if score >= 60 else '不及格'
print(result)
