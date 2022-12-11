import json


def activityLevel(old: int, operator: str) -> int:
    operator = operator.split(" ")[2:]
    for i in range(0, 3, 2):
        if operator[i] == "old":
            operator[i] = old

    if operator[1] == '+':
        return (operator[0] + int(operator[2]))//3
    elif operator[1] == '*':
        return (operator[0] * int(operator[2]))//3


with open("Day 11/input.json", "r") as f:
    f = f.read()
    f = json.loads(f)

    monkeys = [i["Starting items"] for i in f]
    monkey_activity = [0, 0, 0, 0, 0, 0, 0, 0]

    for _ in range(20):
        print("Round")
        for monkey in range(len(monkeys)):
            for _ in range(len(monkeys[monkey])):
                monkey_activity[monkey] += 1
                activity = activityLevel(
                    monkeys[monkey].pop(), f[monkey]["Operation"])
                if activity % f[monkey]["Test"]:
                    monkeys[f[monkey]["If false"]].append(activity)
                else:
                    monkeys[f[monkey]["If true"]].append(activity)
    print(monkey_activity)
