numbers = []
with open('input.txt', 'r') as f:
  numbers = [int(n) for n in f.read().split('\n') if n]

for n in numbers:
  for m in numbers:
    for k in numbers:
      if n + m + k == 2020:
        print(n * m * k)