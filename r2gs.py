#
# This will convert raw data to gameshark codes!
#
import sys

with open(sys.argv[1], "r") as file_content:
    lines = file_content.readlines()
    org = 0x80000000
    gsc = 0x01000000
    pc = 0x0

    for line in lines:
        org_directive = line.find(".org")
        if org_directive >= 0:
            org = int(line[5:].strip(), 16)
            continue
        if line.find(";") >= 0:
            continue
        first_half_word = line[:4]
        last_half_word = line[4:]
        print("{0} {1}".format(hex(org+gsc+pc)[2:], first_half_word))
        pc += 2
        print("{0} {1}".format(hex(org+gsc+pc)[2:], last_half_word))
        pc += 2

