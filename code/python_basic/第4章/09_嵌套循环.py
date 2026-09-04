day = 1
for day in range(1, 31):
    print(f'********第{day}天训练********')
    for group in range(1, 4):
        print(f'第{group}组仰卧起坐训练')
    print(f'第{day}天任务已完成\n')
print(f'为期{day}天训练已完成，我真棒')

day=1
while day<=30:
    print(f'********第{day}天训练********')
    group=1
    while group<=3:
        print(f'第{group}组仰卧起坐训练')
        group+=1
    print(f'第{day}天任务已完成\n')
    day+=1
print(f'为期{day-1}天训练已完成，我真棒')