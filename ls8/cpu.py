"""CPU functionality."""

import sys

# PC: Program Counter, address of the currently executing instruction
# IR: Instruction Register, contains a copy of the currently executing instruction
# MAR: Memory Address Register, holds the memory address we're reading or writing
# MDR: Memory Data Register, holds the value to write or the value just read
# FL: Flags


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256    # 256 bytes of RAM
        self.reg = [0] * 8      # 8 registers
        self.pc = 0             # program counter
     
       
        

    def ram_read(self, MAR):
        return self.ram[MAR]
    
    def ram_write(self, MDR, MAR):
        self.ram[MAR] = MDR

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
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

        LDI     =   0b10000010
        PRN     =   0b01000111
        HLT     =   0b00000001

        running = True

        while running:
            ir = self.ram[self.pc]

            if ir == HLT:
                running = False
                self.pc+=1
                

            elif ir == PRN:
                num = self.reg[self.ram_read(self.pc +1)]
                print(num)
                self.pc+=2


            elif ir == LDI:
                reg_a = self.ram_read(self.pc + 1)
                # print(reg_a)
                reg_b = self.ram_read(self.pc + 2)
                # print(reg_b)
                self.reg[reg_a] = reg_b
                self.pc+=3

            else:
                print(f"Unknown instructions {ir}")
                sys.exit(1)

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
    
