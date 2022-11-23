import re

def part1():
    things = []
    with open("dax2_21.txt", "r", encoding="utf8") as f:
        for line in f.read().splitlines():
            things.append(line)

        x = 0
        y = 0

        for i in range(len(things)):
            if "forward" in things[i]:
                x += int((re.findall(r'\d+',things[i])[0]))

            elif "up" in things[i]:
                y -= int((re.findall(r'\d+',things[i])[0]))

            elif "down" in things[i]:
                y += int((re.findall(r'\d+',things[i])[0]))

        print(x, y)

def part2():
    with open("2021_day2.txt", "r", encoding="utf8") as f:
        lines = f.readlines()
        commands = [entry.strip() for entry in lines]

        x, depth, aim = 0, 0, 0
        for command in commands:
            direction, amount = command.split(' ')[0], int(command.split(' ')[1])
            if "forward" in direction:
                x += amount
                depth += aim*amount
            elif "up" in direction: 
                aim -= amount
            elif "down" in direction:
                aim += amount

    print(x * depth)