# # Why do bitwise operations?
# #   * Isolate bits, becausse they represent true or false
# #   * All cryptographers kow how to do is XOR
# #   * Bitwise operations can be faster


# Operation    Boolean Operator       Bitwise Operator
# AND             &&                         &
# OR              ||                         |  
# XOR             none                       ^
# NOT              !                         ~

# ------------------------------------------------------
# AND:
# a = True
# b = False

# (a && b) == False


# a)  0b10000011
#   & 0b01010101
#   ------------
#     0b00000001

# b)  0b00110101
#   & 0b10101010
#   ------------
#     0b00100000
# -------------------------------------------------------
# OR:
# a = True
# b = False
# (a || b) == True


# a)  0b10101110
#   | 0b11010001
#     ----------
#     0b11111111

# b)  0b00101110
#     0b10100110
#     -----------
#     0b10101110
# --------------------------------------------------------
# XOR:
# a = False
# b = True
# (a xor b) == True

# a = True
# b = True
# (a xor b) == False

#     0b10101101
#   ^ 0b00110110
#   ------------
#     0b10011011
#   ------------------------------------------------------
#   NOT:
#   ~ 0b10101010
#   -------------
#     0b01010101

#  -------------------------------------------------------
#  Right Shift Operator:

# rt3 = 0b10101010>>3
# print(rt3)
# rt4 = 0b10101010>>4
# print(rt4)
# rt5 = 0b10101010>>5
# print(rt5)

# # Left Shift Operator:

# lft3 = 0b10101010<<3
# print(lft3)
# lft4 = 0b10101010<<4
# print(lft4)
# lft5 = 0b10101010<<5
# print(lft5)

---------------------------------------------------------
# How can we isolate the leftmost bit?
# Rightshifting

0b10101010 >> 7

---------------------------------------------------------
# Bitmasking:

#  How can we isolate the rightmost bits?
#  Use AND; put 0's over the bits you don't care about
#  and 1's over the ones you do.

          vv
  0b10101010
& 0b00000011
------------
  0b00000010  # You are left with the original values of the bits you wanted

---------------------------------------------------------

# How can we isolate two center bits?
#   1. Rightshift the first nibble (4 bits)
#   2. Mask out the remaining two bits using AND

      vv
  0b10101010>>4  # ob00001010
        0b00001010
    &   0b00000011
------------------
        0b00000010