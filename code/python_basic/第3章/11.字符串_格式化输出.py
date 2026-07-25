name = '张三'
gender = '男'
age = 18
weight = 60.2

# 写法1：加号拼接,只能在字符串之间进行拼接
info1 = '我叫' + name + '，我是' + gender + '生'
print(info1)

# 写法2：使用占位符
# %s占位字符串，%f占位浮点数，%i占位浮点数，%d占位十进制整数，%s万能
info2 = '我叫%s，我是%s生,我体重是%f,我年龄是%d' % (name, gender, weight, age)
info3 = '我叫%s，我是%s生,我体重是%f,我年龄是%i' % (name, gender, weight, age)
info4 = '我叫%s，我是%s生,我体重是%s,我年龄是%s' % (name, gender, weight, age)
info5 = '我叫%s，我是%s生,我体重是%i,我年龄是%i' % (name, gender, weight, age)
print(info2)
print(info3)
print(info4)
print(info5)

# 写法3：使用f-string，官方推荐
info6=f'我叫{name},我是{gender}生,我体重是{weight},我年龄是{age}'
print(info6)