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
PUSH    =   0b01000101
POP     =   0b01000110
CALL    =   0b01010000
RET     =   0b00010001
ADD     =   0b10100000
CMP     =   0b10100111
JEQ     =   0b01010101
JMP     =   0b01010100
JNE     =   0b01010110

##  Algotrithm for adding commands:
##  add code to top
##  add code and function to branchtable
##  add function

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256    # 256 bytes of RAM (memory)
        self.reg = [0] * 8      # 8 registers ==> R0 through R7
        self.pc = 0             # program counter
        self.reg[7] = 0xF4      # stack pointer for push & pop operations
        self.running = True
        self.operand_a = None
        self.operand_b = None

        self.e_flag = None
        self.l_flag = None
        self.g_flag = None

        self.branchtable = {}
        self.branchtable[HLT]   = self.hlt
        self.branchtable[LDI]   = self.ldi
        self.branchtable[PRN]   = self.prn
        self.branchtable[PUSH]  = self.push
        self.branchtable[POP]   = self.pop
        self.branchtable[CALL]  = self.call
        self.branchtable[RET]   = self.ret
        self.branchtable[JEQ]   = self.jeq
        self.branchtable[JMP]   = self.jmp
        self.branchtable[JNE]   = self.jne


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
        return self.ram[MAR]
    

    def ram_write(self, MDR, MAR):
        self.ram[MAR] = MDR


    def alu(self, op, operand_a, operand_b):

        if op == ADD:
            self.reg[operand_a] += self.reg[operand_b]

        elif op == MUL:
                self.reg[operand_a] *= self.reg[operand_b]

        elif op == CMP:
                registerA = self.reg[operand_a]
                registerB = self.reg[operand_b]

                if registerA == registerB:
                    """
                    Set Equal flag (E) to 1, otherwise set it to 0
                    """
                    # print("Equal")
                    self.e_flag = 1
                else:
                    self.e_flag = 0

                     
                if registerA < registerB:
                    """
                    Set the Less-than flag (L) to 1, otherwise set it to 0
                    """
                    # print("Lesser")
                    self.l_flag = 1
                else:
                    self.l_flag = 0
 
                   
                if registerA > registerB:
                    """
                    Set the Greater-than flag (G) to 1, otherwise set it to 0
                    """
                    # print("Greater")
                    self.g_flag = 1
                else:
                    self.g_flag = 0

        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")


    def trace(self):

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

        registers = [None] * 8
        registers[7] = 0xF4
       
        while self.running:
            IR= self.ram[self.pc]   
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)
      

            sets_pc_directly = IR>>4 & 0b0001
            if not sets_pc_directly:
                self.pc += 1 + (IR>>6)


            is_alu_command = IR & 0b00100000            #  classmate's way: checks the 3rd bit
            # is_alu_command = ((IR>>5) & 0b001) == 1   #  Tim's way: delete last 5 & check the 3rd bit

            if is_alu_command:
                self.alu(IR, operand_a, operand_b)
            else:
                self.branchtable[IR](operand_a, operand_b)

    def hlt(self,*_):       #  ==>  " *_ " represents all the unused arguments
        self.running = False

    def ldi(self, operand_a, operand_b):
        self.reg[operand_a] = operand_b

    def prn(self, operand_a, *_):
        print(self.reg[operand_a])
    
    def push(self, operand_a, *_):
        self.reg[7] -= 1
        sp = self.reg[7]
        self.ram[sp] = self.reg[operand_a] 

    def pop (self, operand_a, *_):
        sp = self.reg[7]
        value = self.ram[sp]
        self.reg[operand_a] = value
        self.reg[7] += 1
    
    def call(self, operand_a, *_):
        self.reg[7] -= 1
        sp = self.reg[7]
        return_address = self.pc + 2
        self.ram[sp] = return_address 

        destination_address = self.reg[operand_a]
        self.pc = destination_address

    def ret(self, *_):
        sp = self.reg[7]
        value = self.ram[sp]
        self.pc = value
        self.reg[7] += 1

    def jmp(self, *_):
        """
        Jump to the address stored in the given register
        Set PC to the address stored in the given register
      
        """   
        stored_address = self.ram[self.pc + 1] 
        self.pc = self.reg[stored_address]
       
    def jeq(self, *_):
        """
        If equal flag is set True, 
        jump to the address stored in the given register 
        """
        if self.e_flag == 1:
            self.pc = self.reg[self.ram[self.pc + 1]]
        else:
            self.pc += 2

    def jne(self, *_):
        """
        If equal flag is clear(False),
        jump to the address stored in the given register
        """
        if self.e_flag  == 0:
            self.pc = self.reg[self.ram[self.pc + 1]]
        else:
            self.pc += 2





#-----------------------------------------------------------------------

## Old code :
            # elif IR == HLT:
            #     self.running = False
            #     # could also use sys.exit()

            # # conditionals for HLT, PRN and LDI:
                
            # elif IR == PRN:     # takes a register number and prints out it's contents
            #     # where to get register number?  ==> operand_a
            #     # how to get contents?          ==> inside self.reg
            #     print(self.reg[operand_a])
                
            # elif IR == LDI:     # set a register to a value
            #     # what is the register number?
            #     # what is the value?
            #     # how do I set the register?
            #     self.reg[operand_a] = operand_b

         
              


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
    
  