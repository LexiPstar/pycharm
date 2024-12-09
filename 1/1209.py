# Iteration-->迭代
# 在Python中，迭代是通过for ... in来完成的，而很多语言比如C语言，迭代list是通过下标完成的
# 使用迭代寻找list当中的最小值和最大值：
# def findMinAndMax(L):
#     min=max=L[0]
#     for num in L:
#         if num<min:
#             min=num
#         elif num>max:
#             max=num
#     return min, max
# def find(L):
#     return min(L),max(L)
# print(findMinAndMax(L=[1,2,3,4,5,6,7,8,9]),find(L=[1,2,3,4,5,6,7,8,9]))
from traceback import print_list

# #列表生成式list comprehensions
# l=[x*x for x in range(1,11)]
# print(l)
# #双层循环
# l=[m+n for m in 'ABC' for n in 'DEF']
# print(l)

#大小写转换
#小写
# d=['anD','lsInJ','MNNolIO']
# print([s.lower() for s in d])
#大写
# print([s.upper() for s in d])

#if_else用法
# l=[1,2,3,4,5,6,7,8,9]
# print([x for x in l if x%2==0 ])
# print([x if x%2==0 else x for x in l ])

# L1 = ['Hello', 'World', 18, 'Apple', None]
# def print_list(L):  打印列表每个元素
#     for x in L :
#         print(x)
# print_list(L1)
# L2=[]
# for x in L1:
#     if isinstance(x,str): #判断元素是否为字符串
#         L2.append(x.lower()) #append函数是在list末尾添加元素 lower吧元素转换小写
# print(L2) #打印新列表
#
# if L2 == ['hello', 'world', 'apple']:
#     print('测试通过!')
# else:
#     print('测试失败!')

#生成器generator
# g=(x*x for x in range(10))
# for x in g:
#     print(x)

#斐波那契数
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#
# print(fib(20))

#杨辉三角
def generate_pascals_triangle(n):
    # 创建一个空列表用于存储杨辉三角
    triangle = []

    for i in range(n):
        # 创建当前行，初始为 1
        row = [1] * (i + 1)

        # 填充当前行的中间部分
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        # 将当前行添加到三角形中
        triangle.append(row)

    return triangle


# 输出杨辉三角的前 5 行
# n = 10
# triangle = generate_pascals_triangle(n)
#
# # 打印杨辉三角
# for row in triangle:
#     print(row)


def print_pascals_triangle(n):
    triangle = generate_pascals_triangle(n)

    for row in triangle:
        print(" ".join(map(str, row)).center(n * 2))


# 打印杨辉三角（美化输出）
print_pascals_triangle(5)

