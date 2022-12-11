import json
from numba import jit, cuda


def activityLevel(old: int, operator: str) -> int:
    operator = operator.split(" ")[2:]
    for i in range(0, 3, 2):
        if operator[i] == "old":
            operator[i] = old

    if operator[1] == '+':
        return (operator[0] + int(operator[2]))
    elif operator[1] == '*':
        return (operator[0] * int(operator[2]))


def doPermutations():
    for _ in range(100000):
        for monkey in range(len(monkeys)):
            while monkeys[monkey]:
                monkey_activity[monkey] += 1
                activity = activityLevel(
                    monkeys[monkey].pop(), f[monkey]["Operation"])
                if activity % f[monkey]["Test"]:
                    monkeys[f[monkey]["If false"]].append(activity % 9_699_690)
                else:
                    monkeys[f[monkey]["If true"]].append(activity % 9_699_690)


with open("Day 11/input.json", "r") as f:
    f = f.read()
    f = json.loads(f)

    monkeys = [i["Starting items"] for i in f]
    monkey_activity = [0, 0, 0, 0, 0, 0, 0, 0]

    doPermutations()

    monkey_activity.sort()
    print(monkey_activity)
