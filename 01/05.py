#定义变量接受年份，判断男子是否成年，如果成年则显示一些东西否则不显示。
# age = int(input('输入年龄：'))
# if age >= 18 :
#     print('你成年了')
# else :
#     print('你是小屁孩')
#
score = int(input('成绩：'))
# if 60 <= score < 80:
#     print('\t及格')
# else :
#     if 80 <= score < 90:
#         print('\t优秀')
#     else :
#         if score >= 90:
#             print('\t完美')
#         else :
#             print('\t打死你')
# while 0 <= score <= 100 :
#     if 60 <= score < 80 :
#         print('\t及格')
#     elif 80 <= score < 90 :
#         print('\t优秀')
#     elif 90 <= score :
#         print('\t完美')
#     elif 0 <= score < 60 :
#         print('\t打死你')
#         break
# else :
#     print('请输入0-100的分数！')

while 0 <= score <= 100:
    if 0 <= score < 60:
        print('\t打死你')
        break
    elif 60 <= score < 80 :
        print('\t及格')
    elif 80 <= score < 90:
        print('\t优秀')
    elif 90 <= score:
        print('\t完美')
else:
    print('非法输入，请输入0-100的分数！')