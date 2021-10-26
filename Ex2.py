mas = int(input("Введите N: "))
array = []
min_ = float('inf')
for i in range(mas):
    num = float(input(f"Введите array[{i}] элемент: "))
    array.append(num)
    if abs(num) < abs(min_):
        min_ = num
print(f"Минимальное по модулю число: {min_}")
minimum = array[0]
for i in range(1, len(array)):
    if array[i] < minimum:
        minimum = array[i]
print("наибольший нечетный элемент", minimum)


