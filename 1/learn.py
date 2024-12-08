import math
# print('1024 * 768 =',1024*768)
# print('''line1
# line2
# line3'''')
# a=123
# b='abc'
# print(a,b)
# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,Bob!'''
# print(n,f,'Hello World','Hello World,\'Adam\'',r'hello world,"bart"',r'''hello,bob!'''')
# x=b'abc'
# print(x)
# r=2.5
# s=3.14*r**2
# print('%s'%s)
# s1=72
# s2=85
# r=(s2-s1)/72
# print('%.1f'%r)
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Bob']
# ]
# print(L[0][0],L[1][1],L[2][2])
# birth = int(input('birth: '))
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')
# height = 1.75
# weight = 80.5
# bmi =weight/height**2
# if bmi<18.5:
#     print("过轻")
# elif bmi in(18.5,25):
#     print("正常")
# elif bmi in(25,28):
#     print("过重")
# elif bmi in(28,32):
#     print("肥胖")
# else:
#     print("严重肥胖")

# age = int(input())
# match age:
#     case x if x < 10:
#         print(f'< 10 years old: {x}')
#     case 10:
#         print('10 years old.')
#     case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
#         print('11~18 years old.')
#     case 19:
#         print('19 years old.')
#     case _:
#         print('not sure.')

# args = ['gcc', 'hello.c', 'world.c']
# # args = ['clean']
# # args = ['gcc']
#
# match args:
#     # 如果仅出现gcc，报错:
#     case ['gcc']:
#         print('gcc: missing source file(s).')
#     # 出现gcc，且至少指定了一个文件:
#     case ['gcc', file1, *files]:
#         print('gcc compile: ' + file1 + ', ' + ', '.join(files))
#     # 仅出现clean:
#     case ['clean']:
#         print('clean')
#     case _:
#         print('invalid command.')

# L = ['Bart', 'Lisa', 'Adam']
# for L in['Bart', 'Lisa', 'Adam']:
#     print(L)

# a={'a','b','c'}
# a.remove('a')
# print(a)

# a=abs(-99)
# print(a)
# b=max(1,2,3,9,8,5,6,4,1)
# print(b)
# c=str(1.23)
# print(c)
# n1 = 255
# n2 = 1000
# s=hex(n1)
# k=hex(n2)
# print(s,k)

# n=int(input())
# def my_abs(m):
#     if m>0:
#         return 'true'
#     else:
#         return 'false'
# print(my_abs(n))
# import math
# def quadratic(a, b, c):
#     x1=-b+math.sqrt(b**2-a*c*4)
#     x2=-b-math.sqrt(b**2-a*c*4)
#     return x1,x2
# print('quadratic(2,3,1)=',quadratic(2,3,1))
# print('quadratic(1,3,-4)=',quadratic(1,3,-4))
# if quadratic(2, 3, 1) != (-0.5, -1.0):
#     print('测试失败')
# elif quadratic(1, 3, -4) != (1.0, -4.0):
#     print('测试失败')
# else:
#     print('测试成功')

# x=int(input())
# y=int(input())
# def power(n,m):
#     s=1
#     while m>0:
#         m-=1
#         s*=n
#     return s
# print(power(x,y))

# name=str(input())
# sex=str(input())
# age=int(input())
# addres=str(input())
# tel=str(input())
# def people_information(name,sex,age,addres,tel):
#     print('name:',name)
#     print('sex:',sex)
#     print('age:',age)
#     print('addres:',addres)
#     print('tel:',tel)
# print(people_information(name, sex, age, addres, tel))

# def mul(*args):
#     if not args:
#         raise TypeError("mul() requires at least one argument")
#     result=1
#     for num in args:
#         result *= num
#     return result
#
# # 测试
# print('mul(5) =', mul(5))
# print('mul(5, 6) =', mul(5, 6))
# print('mul(5, 6, 7) =', mul(5, 6, 7))
# print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
# if mul(5) != 5:
#     print('mul(5)测试失败!')
# elif mul(5, 6) != 30:
#     print('mul(5, 6)测试失败!')
# elif mul(5, 6, 7) != 210:
#     print('mul(5, 6, 7)测试失败!')
# elif mul(5, 6, 7, 9) != 1890:
#     print('mul(5, 6, 7, 9)测试失败!')
# else:
#     try:
#         mul()
#         print('mul()测试失败!')
#     except TypeError:
#         print('测试成功!')
#
# def mul(*args):
#     if not args:  # 检查是否传入了参数
#         raise TypeError("mul() requires at least one argument")
#     result = 1
#     for num in args:
#         result *= num
#     return result
#
# # 测试
# print('mul(5) =', mul(5))                # 输出: mul(5) = 5
# print('mul(5, 6) =', mul(5, 6))          # 输出: mul(5, 6) = 30
# print('mul(5, 6, 7) =', mul(5, 6, 7))    # 输出: mul(5, 6, 7) = 210
# print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))  # 输出: mul(5, 6, 7, 9) = 1890
#
# if mul(5) != 5:
#     print('mul(5)测试失败!')
# elif mul(5, 6) != 30:
#     print('mul(5, 6)测试失败!')
# elif mul(5, 6, 7) != 210:
#     print('mul(5, 6, 7)测试失败!')
# elif mul(5, 6, 7, 9) != 1890:
#     print('mul(5, 6, 7, 9)测试失败!')
# else:
#     try:
#         mul()  # 测试未传参数的情况
#         print('mul()测试失败!')
#     except TypeError:
#         print('测试成功!')
