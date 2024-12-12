#会员/非会员  折扣/非折扣
# vip = input('是否为会员Y/N：')
# money = int(input('消费金额：'))
# if vip == 'Y' or vip == 'y':
#     if money >= 200:
#         print(f'打8折,折后价为{money*0.8}')
#     else:
#         print(f'打9折,折后价为{money*0.9}')
# else:
#     if money >= 200:
#         print(f'打8.8折,折后价为{money*0.88}')
#     else:
#         print('不打折')

# month = int(input('请输入月份：'))
# if month == 3 or month == 4 or month == 5:
#     print('该月份在春季！')
# elif month == 6 or month == 7 or month == 8:
#     print('该月份在夏季！')
# elif month == 9 or month == 10 or month == 11:
#     print('该月份在秋季！')
# elif month == 1 or month == 2 or month == 12:
#     print('该月份在冬季！')
# else:
#     print('输入无效的月份！')  # To handle invalid input (e.g., months outside 1-12)

month = int(input('请输入月份：'))
if month in [1, 2, 12]:
    print('该月份在冬季！')
elif month in [3, 4, 5]:
    print('该月份在春季！')
elif month in [6, 7, 8]:
    print('该月份在夏季！')
elif month in [9, 10, 11]:
    print('该月份在秋季！')
else:
    print('输入无效的月份！')  # 处理无效的输入（例如月份超过1到12）

