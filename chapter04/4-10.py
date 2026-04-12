my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream', 'burger', 'sushi']

print("The first three items in the list are:")
print(my_foods[:3])

# 确定中间是哪个索引号
# my_foods[mid-1 : mid+2]
mid = len(my_foods) // 2

print("\nThree items from the middle of the list are:")
print(my_foods[2:5])

print("\nThe last three items in the list are:")
print(my_foods[-3:])
