

with open("input.txt") as f:
    data = f.read().split("\n")

data = [[int(c) for c in d] for d in data]
trees = 0
for i in  range(len(data)):
    for j in range(len(data[0])):
        if i == 0 :
            trees += 1
        elif j == 0 :
            trees += 1
        elif i == len(data)-1:
            trees += 1
        elif j == len(data[0])-1:
            trees +=1
        elif data[i][j] > max(data[i][:j]) or data[i][j] > max(data[i][j+1:]) or \
            data[i][j] > max([d[j] for d in data[:i]]) or data[i][j] > max([d[j] for d in data[i+1:]]):
            trees += 1

print(trees)

score = 0
for i in  range(len(data)):
    for j in range(len(data[0])):
        if i == 0 :
            continue
        elif j == 0 :
            continue
        elif i == len(data)-1:
            continue
        elif j == len(data[0])-1:
            continue
        else:
            tree = data[i][j]
            cur_score = 1
            l1 = data[i][:j]
            l2 = data[i][j+1:]
            l3 = [d[j] for d in data[:i]]
            l4 = [d[j] for d in data[i+1:]]
            l1.reverse()
            l3.reverse()
            lists = [l1,l2,l3,l4]
            for l in lists:
                distance = 0
                for t in l:
                    distance += 1
                    if t>=tree:
                        break
                cur_score *= distance
            if score < cur_score:
                score = cur_score

print(score)
            