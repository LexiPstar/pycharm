# import random
# num = (random.randint) %100

#石头剪刀布 1.石头 2.剪刀 3.布
import random
computer = random.randint(1,3)
person = int(input('输入数字：'))
if person not in[1,2,3]:
    print('数字无效，请输入1-3的整数！')
else:
    if person == computer:
        print('不输不赢')
    elif person == 1:
        if computer == 2:
            print('人赢')
        elif computer == 3:
            print('电脑赢')
    elif person == 2:
        if computer == 1:
            print('电脑赢')
        elif computer == 3:
            print('人赢')
    elif person == 3:
        if computer == 1:
            print('人赢')
        elif computer == 2:
            print('电脑赢')








# if  computer == person :
#     print('不输不赢')