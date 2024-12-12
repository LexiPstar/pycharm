#while循环
#打印10次   我爱北京天安门
# i = 0
# while i<10:
#     print('我爱北京天安门',i)
#     i += 1

#打印0-10之间的整数  遍历n-m的数  50-72
# i = 0
# n = 50
# while i < 22:
#     if n % 2 == 1:
#         print(n,end='\t')
#         i += 1
#         n += 1
#     else:
#         i += 1
#         n += 1

#1-100之间的偶数
# i = 0
# n = 1
# sum = 0
# print('i   n')
# while i<100:
#     if n%2==0:
#         sum+=n
#         print(n,end='\t')
#     i+=1
#     n+=1
#     print(i,end='\n')
# print(sum,end='\n')

#猜鸡蛋（至少有2个鸡蛋）筐的容量为500
#两个两个数多一个  count % 2 == 1
#三个三个数多一个  count % 3 == 1
# 四个四个数多一个 count % 4 == 1
#请问最多有多少个鸡蛋？
count = 2
while True:
    if count % 2 == 1 and count % 3 == 1 and count % 4 == 1:
        print(f'一共有{count}个鸡蛋',end='\t')
        print(f'count={count}')
    count += 1
    if count > 500:
        break