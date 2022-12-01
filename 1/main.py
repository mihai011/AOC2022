
data = ""
with open("input.txt") as file:
    data = file.read().split("\n\n")
    data = [d.split("\n") for d in data]

elves = {}
for index, group in enumerate(data):
    elves[index] = [int(cal) for cal in group]

max_sum = max(sum(cals) for cals in elves.values())
print(max_sum)

top_three_sum = [sum(cals) for cals in elves.values()]
top_three_sum.sort()
print(sum(top_three_sum[-3:]))