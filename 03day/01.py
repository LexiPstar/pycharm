#else语句
#if...else...中，条件不满足if执行else
# while...else... 和 for...else...中，没有遇到break时执行else
#书三次密码，三次过后 冻结账户

for i in range(3):
    password = input('输入密码：')
    if password == '666666':
        print('密码输入正确！')
        break
    else:
        if i < 2:
            print(f'密码输入错误，您还有{2-i}次输入机会，请重新输入！')

else:
    print('密码输入错误3次，该账户已被冻结，请联系管理员！')
