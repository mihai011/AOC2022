with open("input.txt") as f:
    data = f.read().split("\n")

score = 0
for d in data:
    set1 = d[:len(d)//2]
    set2 = d[len(d)//2:]
    common_characters = ''.join(
    set(set1).intersection(set2)
    )
    for c in common_characters:
        if c.islower():
            score += ord(c) - (ord('a')-1)
        else:
            score += ord(c) - (ord('A')-27)

print(score)
score = 0
for i in range(0,len(data),3):
    set1 = data[i]
    set2 = data[i+1]
    set3 = data[i+2]
    common_characters_2 = ''.join(
    set(set1).intersection(set2)
    )
    common_characters_3 = ''.join(
    set(common_characters_2).intersection(set3)
    )
    for c in common_characters_3:
        if c.islower():
            score += ord(c) - (ord('a')-1)
        else:
            score += ord(c) - (ord('A')-27)

print(score)