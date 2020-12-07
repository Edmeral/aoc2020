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
        Takes an entry line and returns [(bag, containers)]
    """
    entry = entry.split(' ')
    container = ' '.join(entry[0:2])
    rest = ' '.join(entry[4:]).replace(', ', ',').split(',')
    
    if len(rest) == 1: # does not contain bag
        if 'no' in rest[0]:
            return [(None, container)]
        return [(' '.join(rest[0].split(' ')[1:3]), container)]
    
    descendents = [' '.join(s.split(' ')[1:3]) for s in rest]

    parsed_entry = []
    for bag in descendents:
        parsed_entry.append((bag, container))
    return parsed_entry


def get_containers(bag, bags, containers):
    if bag not in bags:
        return containers.add(bag)
    for container in bags[bag]:
        containers.add(container)
        get_containers(container, bags, containers)


with open('input.txt', 'r') as f:
    bags = {} # bag: parent
    for line in f.readlines():
        parsed_entry = parse_entry(line)
        for bag, container in parsed_entry:
            try:
                bags[bag].append(container)
            except KeyError:
                bags[bag] = [container]
    containers = set()
    get_containers('shiny gold', bags, containers)
    print(len(containers))