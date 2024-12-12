name=1123  #整型
print(f'name={name},type={type(name)}')
a=3.6 #浮点型
print(f'a={a},type={type(a)}')
klk_op=True #布尔型
print(f'klk_op={klk_op},type={type(klk_op)}')

#字符串,三种格式   1.''  2.""   3.''' '''（适用于多行书写）   嵌套使用明显

nam='6'
print(f'nam={nam},type={type(nam)}')
cni="6565"
print(f'cni={cni},type={type("cni")}')
cnt='''6'''
print(f'cnt={cnt},type={type('''cnt''')}')


#列表，有序、重复、可扩展
#元组，有序、重复、不可扩展
kuple=['1','2','5','6','1']
print(f'kuple={kuple},type={type(kuple)}')

kuple=('1','2','3')
print(f'kuple={kuple},type={type(kuple)}')

#集合,无序、不可重复、可扩展

kuple={'1','2','3','2','1'}
print(f'kuple={kuple},type={type(kuple)}')

#字典,key>value