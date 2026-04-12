cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)

#第二种方法
cubes = []
for value in range(1,11):
    cubes.append(value**3)

print(cubes)
