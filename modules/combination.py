def combination(total, num):
    source = []
    target = []
    temp = []

    for i in range(total):
        source.append(i+1)

    cycle(source, target, temp, num, 0)
    return target

def cycle(source, target, temp, num, index):
    if len(temp) == num:
        target.append(temp.copy())
        return

    while index < len(source):
        temp.append(source[index])
        index += 1
        cycle(source, target, temp,num, index)
        temp.pop(-1)

arrs = combination(4, 3)
for arr in arrs:
    print(arr)