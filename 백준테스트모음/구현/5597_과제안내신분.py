array = [1 for _ in range(31)]
for _ in range(28):
    array[int(input())] -= 1

for i in range(1,31):
    if array[i] == 1:
        print(i)
