array = [4, 0, 5, 0, 3, 0, 0, 5]
size_init = len(array)
array = [item for item in array if item != 0]
for i in range(size_init - len(array)):
    array.append(0)
print(array)