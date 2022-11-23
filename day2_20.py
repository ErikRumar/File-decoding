import re

with open("day2_20.txt", "r", encoding= "utf8") as f:
    valid = 0
    for line in f.readlines():
        info = line.split(" ")

        amount = [info[0].split("-")]
        count = 0
        for char in info[2]:
            if char == info[1].replace(":", ""):
                count += 1
                print(amount)
        if count >= int(amount[0][0]) and count <= int(amount[0][1]):
            valid += 1

print(valid)
