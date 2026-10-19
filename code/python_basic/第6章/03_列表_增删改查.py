# # 新增
# # 方式一：用列表的append方法，在列表尾部增加一个元素
# nums = [10, 20, 30, 40]
# nums.append(50)
# print(nums)

# # 方式二：用列表的insert方法，在列表指定下标处增加一个元素
# nums = [10, 20, 30, 40]
# nums.insert(2, 777)
# print(nums)

# # 方式三：用列表的extend方法，将可迭代对象中内容取出，追加到列表尾部
# nums = [10, 20, 30, 40]
# nums.extend('番茄炒蛋')
# nums.extend(range(1,4))
# nums.extend([70,80,90])
# print(nums)

# # 删除
# # 方式一：用列表的pop方法，删除指定位置元素，并返回该元素
# nums = [10, 20, 10, 40, 50]
# result = nums.pop(1)
# print(nums)
# print(result)
#
# # 方式二：用列表的remove方法，删除列表中第一次出现的指定值
# nums = [10, 20, 10, 40, 50]
# nums.remove(10)
# print(nums)
#
# # 方式三：用列表的clear方法，删除列表中所有元素
# nums = [10, 20, 10, 40, 50]
# nums.clear()
# nums.clear()
# print(nums)
#
# # 方式四：用del关键字，删除指定元素
# nums = [10, 20, 10, 40, 50]
# del nums[3]
# print(nums)

# # 修改
# nums = [10, 20, 10, 40, 50]
# nums[2]=66
# print(nums)

# # 查询
# nums = [10, 20, 10, 40, 50]
# print(nums[3])