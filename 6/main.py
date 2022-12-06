with open("input.txt") as f:
    data = f.read()



for i in range(0, len(data), 1):
    if len(set(data[i:i+4])) == len(data[i:i+4]):
        print(i+4)
        break

for i in range(0, len(data), 1):
    if len(set(data[i:i+14])) == len(data[i:i+14]):
        print(i+14)
        break
