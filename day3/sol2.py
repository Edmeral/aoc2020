# Right 1, down 1.
# Right 3, down 1.
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.

from functools import reduce

def count_trees(slope, area):
    x = y = count = 0
    while y < len(area) - 1:
        x += slope[0]
        x = x % len(area[0])
        y += slope[1]
        if area[y][x] == '#':
            count += 1
    return count

with open('input.txt', 'r') as f:
    lines = f.read().split('\n')[0:-1]
    lines = list(map(lambda line: list(line), lines))
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    result = reduce(lambda x, y: x * y, [count_trees(slope, lines) for slope in slopes])
    print(result)