#存款 取款
deposit = 1000
withdraw_money = int(input('输入需要取款金额：'))
balance= deposit-withdraw_money
if withdraw_money < deposit:
    deposit -= withdraw_money
    print('你已成功取出 %.2f元'%withdraw_money)
    print('您的余额为： %.2f元'%deposit)
else:
    print('您的存款金额不足%.2f元'%withdraw_money)
    print('您的当前余额为：%.2f元'%deposit)
choice = input('是否退卡YES/NO：')
if choice in ['yes','YES']:
    print('请收好你的磁卡！')
else:
    print('继续操作！')