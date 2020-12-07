"""
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""
from pprint import pp

# if we represent the bags connections as a graph (or is it a tree):
# outermost_bags(b) = set(ancestors(b))
# (if we assume that every ancestor can byitself be an outermost bag)

def parse_entry(entry):
    """
        Takes an entry line and returns [(bag, contents)]
    """
    entry = entry.split(' ')
    container = ' '.join(entry[0:2])
    rest = ' '.join(entry[4:]).replace(', ', ',').split(',')
    
    if len(rest) == 1: # does not contain bag
        if 'no' in rest[0]:
            return (container, [])
        return (container, [(' '.join(rest[0].split(' ')[1:3]), rest[0][0])])
    
    descendents = [(' '.join(s.split(' ')[1:3]), s[0]) for s in rest]

    return (container, descendents)


print(parse_entry('dim aqua bags contain 3 muted indigo bags, 5 vibrant green bags, 3 dotted teal bags.'))


def count(bag, bags):
    if bag not in bags:
        return 1
    else:
        return 1 + sum([int(desc[1]) * count(desc[0], bags) for desc in bags[bag]])


with open('input.txt', 'r') as f:
    bags = {} # bag: parent
    for line in f.readlines():
        bag, descendents = parse_entry(line)
        bags[bag] = descendents
    # print(bags)
    print(count('shiny gold', bags) - 1) 
    # print(containers)46136
    # print(len(containers))