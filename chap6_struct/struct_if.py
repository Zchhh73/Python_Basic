# coding=utf-8
import sys

score = int(sys.argv[1])
if score > 85:
    print('您真优秀！')
if score < 60:
    print('您还需努力！')
if (score >= 60) and (score <= 85):
    print('您的成绩还不错！')
