# 整型是没有小数点的数字，可以是正数、负数、0
import sys

age = 18
temp = -15
score = 0

# 可使用下划线将较大数字分组，增加可读性
salary = 300_000
house_price = 32_000_000
graduates = 12_000_000
print(salary, house_price, graduates)

"""
python中整型数字的上限取决于执行代码的计算机内存和处理能力
python用print函数中打印数字时，内部会将数字转换成字符串再打印，
python中数字转换为字符串默认限制数字不能超过4300位
"""
a = 99999999999999999999999999999999999999999999999999
a = 3 ** 2
a = 9 ** 9999


"""
可使用sys.set_int_max_str_digits(0)这个函数解除print函数转换数字为字符串的4300位限制，
括号内数字写多少限制位数为多少0表示不限制
"""
sys.set_int_max_str_digits(0)
print(a)


b = a + 100
