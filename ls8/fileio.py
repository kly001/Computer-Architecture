# try:
#     file = open('examples/print8.ls8', 'r')
#     lines = file.read()
#     # print(lines)
#     raise Exception("HI")
# except Exception:
#     print(file.closed)

# file.close()
import sys

print(sys.argv)


with open(sys.argv[-1]) as file:
    for line in file:
        print(line)
 