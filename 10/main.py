with open("input.txt") as f:
    data = f.read().split("\n")

reg = [1]

for line in data:
    reg.append(reg[-1])
    line = line.split(" ")
    if line[0] == "addx":
        reg.append(int(line[1]) + reg[-1])
s=0

for x in range(20,260,40):
    s += x*reg[x-1]
print(s)
screen = ""
for i in range(len(reg)):
    if abs(reg[i] - i % 40) <= 1:
        screen += "#"
    else:
        screen += "."

for i in range(7):
    text = screen[i*40: (i+1)*40]
    print(text)

