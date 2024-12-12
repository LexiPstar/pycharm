name='我叫小明'
age=18
print(f'{name},今年{age}岁,请多多关照！')


student_id=1

print('我的学号是%06d'%(student_id,))
print('我的学号是%06d'%student_id)

# %s 表示字符串占位符      %d 整型占位符      %f 浮点数占位符  %c
price = 9.00
weight = 5.00
money = price * weight
print('苹果单价%.2f元,购买了%.2f斤,一共花了%.2f元'%(price,weight,money))

#输出%   需要填写两个%%
scale = 10.00
print('数据比例是 %.2f%%' %scale)

num1=10
num2=20
result=float(num1)+float(num2)
print(f'result=%.2f'%result)