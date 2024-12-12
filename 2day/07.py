#地球和太阳的故事:地球是围绕着太阳转的,每转完一圈是一年.(公转)但是地球绕着太阳转的同时，自己也在转,转一圈是一天.
#(自转)因此，当地球完成一次公转同时,那么地球就已经完成了365 次的自转.

# for s in range(1,2,1):
#     for e in range(1, 366, 1):
#         print(f'地球完成了{e}次自转.')
#     print(f'地球完成了{s}次公转.')

#打印五行五列正方形
# for i in range(5):   #控制行数
#     for j in range(5):   #控制列数
#         print('*',end='\t')
#     print()

#直角三角形
for i in range(5):
    for j in range(i+1):
        print('*',end='\t')
    print()
for i in range(4):
    for j in range(4-i):
        print('*', end='\t')
    print()