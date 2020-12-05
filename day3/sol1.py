# right 3, down 1
with open('input.txt', 'r') as f:
    lines = f.read().split('\n')[0:-1]
    lines = list(map(lambda line: list(line), lines))
    x = y = count = 0
    while y < len(lines) - 1:
        x += 3
        x = x % len(lines[0])
        y += 1
        if lines[y][x] == '#':
            count += 1
    print(count)