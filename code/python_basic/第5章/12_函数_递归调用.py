# 递归打印n次“你好啊”
def welcome(n):
    print(f'你好啊{n}')
    if n > 1:
        welcome(n - 1)

#调用函数
welcome(3)

# 递归打印n次“你好啊”
def welcome(n):
    if n > 1:
        welcome(n - 1)
    print(f'你好啊{n}')
#调用函数
welcome(3)
