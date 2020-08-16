PRINT_TIM      =  0b00000001
HALT           =  0b00000010
PRINT_NUM      =  0b01000011  # command 3
SAVE           =  0b10000100
PRINT_REGISTER =  0b01000101
ADD            =  0b10000110  # command 6
MULT           =  0b10100010


# Rules of our  game
## we store everything in memory
## we move our PC to step through memory, and execute commands

import sys

memory = [None] * 256

running = True
pc = 0

def load_program():
    # address = 0
    # print(sys.argv)
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                comment_split = line.split('#')
                # print(line)

                possible_num = comment_split[0]

                possible_num.strip()

                if possible_num == '':
                    continue

                if possible_num[0] == '1' or possible_num[0] == '0':
                    num = possible_num[:8]
                    # print(f'{num}: {int(num, 2)}')

                    memory[address] = int(num, 2)
                    address += 1


    except FileNotFoundError:
        print(f'{sys.argv[0]}:{sys.argv[1]} not found')

load_program()

# Memory bus
## a bunch of wires that the CPU uses to send an address to RAM
## also a data bus: CPU sends data to RAM, RAM sends data to CPU
##     CPU
##  ||||||||
##  ||||||||
##  ||||||||
##     RAM

# 0b00000001
# 0b00000010
# 0b11111111

# save the number 42 into R2
# what arguments does SAVE require?

# registers (use as variables)
# R0-R7

registers = [None] * 8
registers[7] = 0xF4

while running:

    command = memory[pc]

    num_operands = command >> 6

    if command == PRINT_TIM:
        print("Tim!")

    elif command == PRINT_NUM:
        number_to_print = memory[pc + 1]
        print(number_to_print)

    elif command == SAVE:
        num = memory[pc + 1]
        index = memory[pc + 2]
        registers[index] = num

    elif command == PRINT_REGISTER:
        reg_idx = memory[pc + 1]
        print(registers[reg_idx])


    elif command == ADD:
        first_reg_idx = memory[pc + 1]
        second_reg_idx = memory[pc + 2]

        registers[first_reg_idx] += registers[second_reg_idx]

    elif command == HALT:
        running = False

    # what if we set the pc directly?
    pc += num_operands + 1

#-------------------------------------------------------------------------------
