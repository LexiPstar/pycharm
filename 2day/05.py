#统计1-100之间3的倍数的数
i = 1
count = 0
while True:
    if i % 3 == 0:
        count += 1
        print(i,end=' ')
    i += 1
    if i > 100:
        break
print(f'count={count}')