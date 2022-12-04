with open("input.txt") as f:
    data = f.read().split("\n")

new_data = []

for d in data:
    inters = d.split(",")
    inter1 = int(inters[0].split("-")[0]),int(inters[0].split("-")[1])
    inter2 = int(inters[1].split("-")[0]),int(inters[1].split("-")[1])
    new_data.append((inter1, inter2))

score = 0

for inters in new_data:

    if inters[0][0] >= inters[1][0] and inters[0][0] <= inters[1][1] and \
        inters[0][1] >= inters[1][0] and inters[0][1] <= inters[1][1]:
        score +=1
        continue
    if inters[1][0] >= inters[0][0] and inters[1][0] <= inters[0][1] and \
        inters[1][1] >= inters[0][0] and inters[1][1] <= inters[0][1]:
        score +=1
        continue

print(score)

score = 0

for inters in new_data:

    if inters[0][0] >= inters[1][0] and inters[0][0] <= inters[1][1] or \
        inters[0][1] >= inters[1][0] and inters[0][1] <= inters[1][1]:
        score +=1
        continue
    if inters[1][0] >= inters[0][0] and inters[1][0] <= inters[0][1] or \
        inters[1][1] >= inters[0][0] and inters[1][1] <= inters[0][1]:
        score +=1
        continue

print(score)