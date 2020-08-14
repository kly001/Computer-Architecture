"""CPU functionality."""

import sys

# PC: Program Counter, address of the currently executing instruction
# IR: Instruction Register, contains a copy of the currently executing instruction
# MAR: Memory Address Register, holds the memory address we're reading or writing
# MDR: Memory Data Register, holds the value to write or the value just read
# FL: Flags

LDI     =   0b10000010
PRN     =   0b01000111
HLT     =   0b00000001
MUL     =   0b10100010 


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256    # 256 bytes of RAM (memory)
        self.reg = [0] * 8      # 8 registers ==> R0 through R7
        self.pc = 0             # program counter
        self.running = True
     
    # def load(self):
        """Load a program into memory."""
        # # For now, we've just hardcoded a program:
        # address = 0

        # program = [
        #     # From print8.ls8
        #     0b10000010,  # LDI R0,8 (load a number into a register)
        #     0b00000000,  # R0
        #     0b00001000,  # 8 (value to print)
        #     0b01000111,  # PRN R0
        #     0b00000000,  # Register 0
        #     0b00000001,  # HLT
        # ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1

#------------------------------------------------------------------------------
# # Unhardcode the Machine Code


    def load(self, filename):
        address = 0
        # print(address)
        try:
            with open(filename) as file:
                for line in file:
                    # print(line)
                    comment_split = line.split('#')
                    possible_num = comment_split[0]

                    if possible_num == '':
                        continue

                    if possible_num[0] == '1' or possible_num[0] == '0':
                        num = possible_num[:8]
                        # print(f'{num}: {int(num, 2)}')

                        self.ram[address] = int(num, 2)
                        address += 1

        except FileNotFoundError:
            print(f'{sys.argv[0]}:{sys.argv[1]} not found')     
        

    def ram_read(self, MAR):
        """
        accepts address to read
        returns value stored there
        """
        return self.ram[MAR]
    
    def ram_write(self, MDR, MAR):
        """
        acccepts value to write and adress to write it to
        writes value to memory at that address
        """
        self.ram[MAR] = MDR

    

    def alu(self, op, operand_a, operand_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[operand_a] += self.reg[operand_b]
        elif op == MUL:
                self.reg[operand_a] *= self.reg[operand_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
       
        while self.running:

         #  get command
            IR= self.ram[self.pc]   # command; where pc is
            # we might not use these, depending on the command.  Get them just in case
            operand_a = self.ram_read(self.pc + 1)
            # print(operand_a)
            operand_b = self.ram_read(self.pc + 2)
            # print(operand_b)

         # update program counter
         # look at the first two bits of the instruction
         #  if the command sets the PC directly, then don't do this:
            self.pc += 1 + (IR>>6)

        #  if IR is an ALU command, send to ALU

            is_alu_command = ((IR>>5) & 0b001) == 1

            if is_alu_command:
                self.alu(IR, operand_a, operand_b)

            elif IR == HLT:
                self.running = False
                # could also use sys.exit()

            # conditionals for HLT, PRN and LDI:
              
            elif IR == PRN:     # takes a register number and prints out it's contents
                # where to get register number?  ==> operand_a
                # how to get contents?          ==> inside self.reg
                print(self.reg[operand_a])
               
            elif IR == LDI:     # set a register to a value
                # what is the register number?
                # what is the value?
                # how do I set the register?
                self.reg[operand_a] = operand_b

         
              


###----------------------------------------------------------------------------

# if __name__ == "__main__":
#     emul = CPU()
#     emul.load()
 
#     # for i in range(9):
#     #     print(emul.ram_read(i))

#     print(emul.ram_read(0))      # 130
#     print(emul.ram_read(1)) 
#     print(emul.ram_read(2))      #  8
#     print(emul.ram_read(3))      # 71
#     print(emul.ram_read(4))
#     print(emul.ram_read(5))      # 1
#     print(emul.ram_read(6)) 
#     print(emul.ram_read(7))
    
