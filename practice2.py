import sys

PRINT_JOAN      = 1
HALT            = 2
PRINT_NUM       = 3
SAVE            = 4 # save a value to a register
PRINT_REGISTER  = 5 # print a value from a register
ADD             = 6 # add the value from a second register into the first register(regA += regB)

memory = [
    PRINT_JOAN,
    PRINT_NUM,
    1,
    SAVE,
    65,
    2,
    SAVE,
    20,
    3,
    ADD,
    2,
    3,
    PRINT_REGISTER,
    2,
    HALT
]

registers = [0] * 8

pc = 0
running = True

while running:
    command = memory[pc]

    if command == PRINT_JOAN:
        print("JOAN !")
        pc += 1
    
    elif command == HALT:
        running = False
        pc += 1

    elif command == PRINT_NUM:
        num = memory[pc + 1]    # gets arguments
        print(num)
        pc += 2

    elif command == SAVE:
        num = memory[pc + 1]
        reg = memory[pc + 2]
        registers[reg] = num
        pc += 3

    elif command == PRINT_REGISTER:
        reg = memory[pc + 1]
        print(registers[reg])
        pc += 2
    
    elif command == ADD:
        reg_a = memory[pc + 1]
        reg_b = memory[pc + 2]
        registers[reg_a] += registers[reg_b]
        pc += 3


    else:
        print(f"Unknown instructions {command}")
        sys.exit(1)
 


