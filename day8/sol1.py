def execute(acc, i, instructions):
    
    instruction = instructions[i]
    opcode = instruction[0]
    val = int(instruction[1])

    instruction[2] = True
    next_pos = i
    if opcode == 'nop':
        next_pos += 1
    if opcode == 'acc':
        acc += val
        next_pos += 1
    if opcode == 'jmp':
        next_pos = i + val

    if instructions[next_pos][2]:
        return (i, acc)

    return execute(acc, next_pos, instructions)
        
with open('test', 'r') as f:
    instructions = f.readlines()
    program = [[instruction.split(' ')[0], instruction.split(' ')[1].strip(), None] for instruction in instructions]
    print(execute(0, 0, program))
    




