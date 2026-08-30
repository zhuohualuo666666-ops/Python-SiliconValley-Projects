print('正确回答逃出密室')
riddle = '你是谁'
answer = '心上人'
guess = ''
while guess != answer:
    print(f'问题：{riddle}')
    guess = input('请输入答案：')
    if guess == answer:
        print('答案正确，拜拜')
    else:
        print('回答错误，继续')