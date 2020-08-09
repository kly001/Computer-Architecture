# PRINT_KAREN         =  0b00000001
# HALT                =  0b00000010
# PRINT_NUM           =  0b00000011 # command 3
# SAVE                =  0b00000100
# PRINT_REGISTER      =  0b00000101
# ADD                 =  0b10000110  # command 6    

# #  Rules of the game:
#     # store everything in memeory
#     # move the pc to step through memory and execute commands

# memory = [
#     PRINT_KAREN,    #  <==  pc starts here
#     PRINT_KAREN,
#     PRINT_NUM,
#     99,
#     SAVE,
#     42, # number to save
#     2,  # register to save into
#     SAVE, 
#     42, # number to save
#     3,  # into R3
#     ADD, # registers [2] = registers[2] + registers[3]
#     2,  # register index
#     3,  # register index
#     PRINT_REGISTER, # should print 84
#     2,
#     HALT,
# ]


# running = True
# pc = 0  # program counter

# # Memory bus
# ## a bunch of wires that the CPU uses to send an address to RAM
# ## also a data bus: CPU sends data to RAM, RAM sends data to CPU

# # save the number 99 into R2
# # What arguments does SAVE require?


# #  registers ( use ad variables)
# #  R0 - R7
# registers = [None] * 8

# while running:
#     command = memory[pc]

#     num_operands = command >> 6

#     if command == PRINT_KAREN:
#         print("KAREN !")

#         pc += 1  # one-byte instruction
    
#     if command == PRINT_NUM:
#         number_to_print = memory[pc + 1]
#         print(number_to_print)

#         pc += 2  #  two-byte instruction

#     if command == SAVE:
#         number_to_save = memory[pc +1]
#         index = memory[pc + 2]
#         registers[index] = number_to_save

#         pc += 3

#     if command == PRINT_REGISTER:
#         register_index = memory[pc + 1]
#         print(registers[register_index])

#         pc += 2
    
#     if command == ADD:
#         first_reg_index =memory[pc + 1]
#         second_reg_index = memory[pc + 2]

#         registers[first_reg_index] += registers[second_reg_index]


#     if command == HALT:
#         running = False

#     pc += num_operands + 1
   
#-------------------------------------------------------------------------------

# operation Codes:

PRINT_KAREN         = 0b00000001
HALT                = 0b00000010
PRINT_NUM           = 0b00000011
SAVE                = 0b00000100



memory = [
    PRINT_KAREN,
    PRINT_KAREN, 
    PRINT_NUM,
    42,
    SAVE,
    99,
    2,
    HALT,
]

# Write a program to pull each command out of memory and execute

# we can loop over it

# register aka memory
registers = [0] * 8

# save the number 99 into R2
# registers ==> R0 - R7

pc = 0 # program counter
running = True
while running:
    command = memory[pc]

    if command == PRINT_KAREN:
        print("Karen is here !")


    if command == HALT:
        running = False

    if command == PRINT_NUM:
        num_to_print = memory[pc + 1]
        print(num_to_print)
 

 
        pc+= 1


    if command == SAVE:
        number_to_save = memory[pc +1]
        index = memory[pc + 2]
        registers[index] = number_to_save


    pc += 1
