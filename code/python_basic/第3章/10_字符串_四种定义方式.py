# 单引号与双引号写法等价，二者不可直接换行，需要加注释，单引号用的多
message1 = ('鸡你'
            '太美')
message2 = ("鸡你"
            "太美")
# 三个单引号写法可直接换行，也可直接作为多行注释使用；三个双引号写法，可以直接换行，也可直接作为多行注释、文档字符串使用
message3 = '''鸡你
太美'''
message4 = """鸡你
太美"""

print(message1)
print(message2)
print(message3)
print(message4)
