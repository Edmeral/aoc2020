def count_yeses(group_entry):
    return len(set(list(''.join(group_entry))))


with open('input.txt', 'r') as f:
    lines = f.readlines()
    group_entries = []
    group_entry = []
    # this looks too complex for what it does..
    for line in lines:
        if line == '\n':
            group_entries.append(group_entry)
            group_entry = []
            continue
        group_entry.append(line.strip())
    group_entries.append(group_entry)
    count = sum([count_yeses(group_entry) for group_entry in group_entries])
    print(count)
