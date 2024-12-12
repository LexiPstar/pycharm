num1 = int(input('请输入数字：'))
num2 = int(input('请输入数字：'))
num3 = int(input('请输入数字：'))
# if num1 > num2:
#     if num1 > num3:
#         print(f'num1={num1}最大')
#     else:
#         print(f'num3={num3}最大')
# else:
#     if num2 < num3:
#         print('f'num3={num3}最大')
#     else:
#         print(f'num2={num2}最大')


second_max = num1 if num1 > num3 else num3
max = second_max if second_max > num2 else num2
print(f'max={max}')