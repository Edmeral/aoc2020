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

    if next_pos == len(instructions):
        return (True, acc)

    if instructions[next_pos][2]:
        return (i, acc)

    return execute(acc, next_pos, instructions)

def reinitialize_acc(program):
    for instruction in program:
        instruction[2] = None


with open('input.txt', 'r') as f:
    instructions = f.readlines()
    program = [[instruction.split(' ')[0], instruction.split(' ')[1].strip(), None] for instruction in instructions]
    # program[7][0] = 'nop'
    execute(0, 0, program)
    for i in range(len(program)):
        instruction = program[i]
        if instruction[0] == 'nop':
            instruction[0] = 'jmp'
            reinitialize_acc(program)
            # print(i, program)
            res = execute(0, 0, program)
            if res[0] == True:
                print(res[1])
                break
            instruction[0] = 'nop'
        if instruction[0] == 'jmp':
            instruction[0] = 'nop'
            reinitialize_acc(program)
            res = execute(0, 0, program)
            # print(i, program)
            if res[0] == True:
                print(res[1])
                break
            instruction[0] = 'jmp'
            
    # print(execute(0, 0, program))
    




