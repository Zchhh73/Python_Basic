#csv数据交换格式
import csv
'''
读取csv文件
with open('list.csv','r',encoding='gbk') as rf:
    rows = []
    reader = csv.reader(rf,dialect=csv.excel)
    for row in reader:
        rows.append('|'.join(row))
    rows = rows[1:]
    print(rows[2].split('|')[-1])
'''
#写入csv文件
with open('list.csv','r',encoding='gbk') as rf:
    reader = csv.reader(rf)
    with open('books.csv','w',newline='',encoding='gbk') as wf:
        writer = csv.writer(wf,delimiter='\t')
        for row in reader:
            print('|'.join(row))
            writer.writerow(row)
