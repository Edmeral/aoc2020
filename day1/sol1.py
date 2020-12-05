# numbers = []
# with open('input.txt', 'r') as f:
#   numbers = [int(n) for n in f.read().split('\n') if n]

# for n in numbers:
#   m = 2020 - n
#   if m in numbers:
#     print(n * m)


numbers = []
numbers_dict = {}

with open('input.txt', 'r') as f:
  numbers = [int(n) for n in f.read().split('\n') if n]

for n in numbers:
  m = 2020 - n
  if m in numbers:
    print(n * m)


