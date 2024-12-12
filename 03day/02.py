'''字符串切片
将原来的字符串进行切割
语法：[start:stop:step]
1.start  开始（从头开始，位置为0）
2.stop   结束（默认到尾）
3.step   步长（默认为1）
必须要确定三个数值。区间为[ , )
字符串下标正向从0开始，逆向从-1开始，index（下标）
-6 -5 -4 -3 -2 -1 (逆序）
 a  b  c  d  e  f
 0  1  2  3  4  5（正序）
 例如：取def
 str[3] >> d         index=3   （这不是切片，是字符索引）
 str[3;5]   这是切片
 start=6  stop=6  step默认为1
 截取为  e  d  f
'''
str = 'abcdef'
print(str[3])
print(str[3:6])
