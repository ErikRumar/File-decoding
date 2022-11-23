import re

#This is part2 completed

things, things2, number = [], [], 0
with open("day1_21.txt", "r", encoding="utf8") as f:
    for line in f.read().splitlines():

        line = int(line)
        things.append(line)


    for i in range(len(things)):
        things2.append(things[i-2]+things[i-1]+things[i])
        if things2[i-1] < things2[i]:
            number += 1
        else:
            continue
print(number)
