import sys

score = int(sys.argv[1])

if score >= 60:
    print('及格')
    if score >= 90:
        print('优秀')
else:
    print('不及格！')
