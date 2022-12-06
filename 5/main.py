import copy

with open("input.txt") as file:
    data = file.read().split("\n\n")

stacks = data[0]
moves = data[1]

data_stacks = stacks.split("\n")
orig_towers = {}
for row in data_stacks[:-1]:
    for i , c in enumerate(row):
        if c.isalpha():
            if int(data_stacks[-1][i]) not in orig_towers:
                orig_towers[int(data_stacks[-1][i])] = [c]        
            else:
                orig_towers[int(data_stacks[-1][i])].append(c)


for key in orig_towers:
    l = orig_towers[key]
    l.reverse()
    orig_towers[key] = l

towers = copy.deepcopy(orig_towers)

for move in moves.split("\n"):
    move = move.split(" ")
    how_many = int(move[1])
    source = int(move[3])
    destination = int(move[-1])
    for _ in range(how_many):
        packet = towers[source].pop()
        towers[destination].append(packet)

view = ""
for k in sorted(towers.keys()):
    view+=towers[k][-1]

towers = orig_towers.copy()
for move in moves.split("\n"):
    move = move.split(" ")
    how_many = int(move[1])
    source = int(move[3])
    destination = int(move[-1])
    packet = []
    for _ in range(how_many):
        packet.append(towers[source].pop())
    packet.reverse()
    towers[destination] += packet
    
view = ""
for k in sorted(towers.keys()):
    view+=towers[k][-1]
print(view)