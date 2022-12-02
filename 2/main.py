
with open("input.txt") as f:
    data = [d.split(" ") for d in f.read().split("\n")]


"""A=ROCK
B=PAPER
C=SCISSORS
X=ROCK
Y=PAPER
Z=SCISSORS
"""

score = 0
for d in data:
    if d[0] == "A" and d[1] == "X":
        score += 3 + 1
    if d[0] == "A" and d[1] == "Y":
        score += 6 + 2
    if d[0] == "A" and d[1] == "Z":
        score += 0 + 3
    if d[0] == "B" and d[1] == "X":
        score += 0 + 1
    if d[0] == "B" and d[1] == "Y":
        score += 3 + 2        
    if d[0] == "B" and d[1] == "Z":
        score += 6 + 3
    if d[0] == "C" and d[1] == "X":
        score += 6 + 1
    if d[0] == "C" and d[1] == "Y":
        score += 0 + 2
    if d[0] == "C" and d[1] == "Z":
        score += 3 + 3

print(score)

score = 0
for d in data:
    if d[0] == "A" and d[1] == "X":
        score += 0 + 3
    if d[0] == "A" and d[1] == "Y":
        score += 3 + 1
    if d[0] == "A" and d[1] == "Z":
        score += 6 + 2
    if d[0] == "B" and d[1] == "X":
        score += 0 + 1
    if d[0] == "B" and d[1] == "Y":
        score += 3 + 2        
    if d[0] == "B" and d[1] == "Z":
        score += 6 + 3
    if d[0] == "C" and d[1] == "X":
        score += 0 + 2
    if d[0] == "C" and d[1] == "Y":
        score += 3 + 3
    if d[0] == "C" and d[1] == "Z":
        score += 6 + 1

print(score)