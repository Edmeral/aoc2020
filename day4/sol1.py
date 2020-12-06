# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID) 
# cid (Country ID)

# hgt:159cm
# pid:561068005 eyr:2025 iyr:2017 cid:139 ecl:blu hcl:#ceb3a1
# byr:1940

from functools import reduce


def is_valid(entry):
    fields = [field.split(':')[0] for field in ' '.join(entry).split(' ')]
    needed_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    return needed_fields.issubset(fields)

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
