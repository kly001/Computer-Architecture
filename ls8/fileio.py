# try:
#     file = open('examples/print8.ls8', 'r')
#     lines = file.read()
#     # print(lines)
#     raise Exception("HI")
# except Exception:
#     print(file.closed)

# file.close()
import sys

if len(sys.argv) < 2:
    print('Did you forget the file to open?')
    print('Usage: filename file_to_open')
    sys.exit()

ram = [None] * 256
address = 0

try:
    with open(sys.argv[1]) as file:
        for line in file:
            comment_split = line.split('#')

            possible_num = comment_split[0]

            if possible_num == '':
                continue

            if possible_num[0] == '1' or possible_num[0] == '0':
                num = possible_num[:8]
                print(f'{num}: {int(num, 2)}')

                ram[address] = int(num, 2)
                address += 1
               

except FileNotFoundError:
    print(f'{sys.argv[0]}:{sys.argv[1]} not found')
 