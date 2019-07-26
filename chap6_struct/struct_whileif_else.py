i = 0

while i * i < 10:
    i += 1
    print("{0} * {0} = {1}".format(i,i*i))
else:
    print("while over!")

print('-----------')

for item in range(10):
    if item == 3:
        break
    print("Count is : {0}".format(item))
else:
    print('For over!')