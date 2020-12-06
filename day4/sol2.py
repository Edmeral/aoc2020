"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""

from functools import reduce


def is_number(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def is_valid_hgt(hgt):
    n = hgt[0:-2]
    if hgt[-2:] == 'cm':
        return is_number(n) and (150 <= int(n) <= 193)
    if hgt[-2:] == 'in':
        return is_number(n) and (59 <= int(n) <= 76)
    return False


def is_valid_hcl(hcl):
    if len(hcl) != 7 or hcl[0] != '#':
        return False
    valid_chars = set(list('0123456789abcdef'))
    return set(list(hcl[1:])).issubset(valid_chars)


rules = {
    'byr': lambda s: len(s) == 4 and is_number(s) and (1920 <= int(s) <= 2002),
    'iyr': lambda s: len(s) == 4 and is_number(s) and (2010 <= int(s) <= 2020),
    'eyr': lambda s: len(s) == 4 and is_number(s) and (2020 <= int(s) <= 2030),
    'hgt': is_valid_hgt,
    'hcl': is_valid_hcl,
    'ecl': lambda s: s in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda s: len(s) == 9 and is_number(s),
}


def is_valid(entry):
    fields = {field.split(':')[0]: field.split(':')[1] for field in ' '.join(entry).split(' ')}
    for key, predicate in rules.items():
        if key not in fields or not predicate(fields[key]):
            return False
    return True

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    entries = []
    entry = []
    for line in lines:
        if line == '':
            entries.append(entry)
            entry = []
        else:
            entry.append(line)
    valid_entries = reduce(lambda  acc, entry: acc + 1 if is_valid(entry) else acc, entries, 0)
    print(valid_entries)