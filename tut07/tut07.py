import os

def checkfile():
    return os.path.exists("input.txt")

count_valid = 0
count_invalid = 0

if checkfile():
    with open("input.txt", 'r') as file:
        for line in file:
            stripped_line = line.strip()
            if "Valid" in stripped_line:
                count_valid += 1
            elif stripped_line:
                count_invalid += 1

print("Valid Passwords:", count_valid)
print("Invalid Passwords:", count_invalid)