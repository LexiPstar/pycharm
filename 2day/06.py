#range(start,stop,step)函数生成序列-->  指定范围     例如：1，2，3，4，5，6，7，8，9.....
#start(开头>=，不指定默认为0)  stop(末尾不包含即不=，<，必须指定)  step(增量,不指定默认为1） 区间为[n,n+2)-->(n,n+1)
# r = range(1,11,1)
# print(f'r = {range(1,11,1)}')
# for i in range(11):  #循环11次  默认从0开始 默认增量为1
#     print(i,end='\t')
# for i in range(1,11):  #循环10次  默认从1开始  默认增量为1
#     print(i,end='\t')
# for i in range(1,11,2):  #循环10次  默认从1开始  默认增量为2
#     print(i,end='\t')

#1-100整数和
range(1,101,1)
sum = 0
for i in range(1,101,1):
    sum += i
print(f'sum={sum}')


sum = 0
i = 1
while i < 101:
    sum += i
    i += 1
print(f'sum={sum}')

count = 0
for i in range(10):
    for i in range(10):
        count += 1
print(f'count={count}')