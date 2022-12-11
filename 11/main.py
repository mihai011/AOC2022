import math

def get_monkeys():

    with open("input.txt") as file:
        data = file.read().split("\n\n")

    monkeys = {}
    tests=[]

    for i,d in enumerate(data):
        monkeys[i] = {}
        d = d.split("\n")
        items = d[1].split(":")[1].split(",")
        monkeys[i]["items"] = [int(item) for item in items]
        operation = d[2].split(":")[1].split(" ")
        op = operation[-2]
        monkeys[i]["op"] = op
        if operation[-1] == "old":
            monkeys[i]["op_val"] = "old"
        else:
            monkeys[i]["op_val"] = int(operation[-1])
        test = d[3].split(":")[1].split(" ")[-1]
        branch_1 = d[4].split(":")[1].split(" ")[-1]
        branch_2 = d[5].split(":")[1].split(" ")[-1]
        monkeys[i]["test"] = int(test)
        tests.append(int(test))
        monkeys[i]["branch_1"] = int(branch_1)
        monkeys[i]["branch_2"] = int(branch_2)
        monkeys[i]["times"] = 0
        monkeys[i]["last_times_inc"] = []

    return monkeys, tests

def func(monkeys, rounds, worry_div, mod_div=None):

    for _ in range(rounds):
        for monkey in monkeys:
            monkeys[monkey]["times"] += len(monkeys[monkey]["items"])
            monkeys[monkey]["last_times_inc"].append(len(monkeys[monkey]["items"]))
            for item in monkeys[monkey]["items"]:
                if monkeys[monkey]["op"] == "*" and monkeys[monkey]["op_val"] == "old":
                    worry = item ** 2
                elif monkeys[monkey]["op"] == "*":
                    worry = item * monkeys[monkey]["op_val"]
                elif monkeys[monkey]["op"] == "+":
                    worry = item + monkeys[monkey]["op_val"]
                elif monkeys[monkey]["op"] == "-":
                    worry = item - monkeys[monkey]["op_val"]
                elif monkeys[monkey]["op"] == "/":
                    worry = item / monkeys[monkey]["op_val"]
                worry = worry//worry_div
                if mod_div:
                    worry = worry%mod_div
                else:
                    worry = worry//worry_div
                if worry % monkeys[monkey]["test"] == 0:
                    next_monkey = monkeys[monkey]["branch_1"]
                else:
                    next_monkey = monkeys[monkey]["branch_2"]
                monkeys[next_monkey]["items"].append(worry)
                
            monkeys[monkey]["items"] = []
        # print(monkeys)
    full_times = []
    for monkey in monkeys:
        full_times.append(monkeys[monkey]["times"])

    full_times.sort()
    print(full_times[-1]*full_times[-2])

if __name__ == "__main__":
    monkeys, tests = get_monkeys()
    mod_lcm = math.lcm(*tests)
    func(monkeys, 10000, 3, mod_lcm)
    monkeys, tests = get_monkeys()
    func(monkeys, 10000, 1, mod_lcm)