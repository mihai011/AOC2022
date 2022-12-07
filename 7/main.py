class Node:

    def __init__(self, dir_name,contents,parent) -> None:
        self.dir_name = dir_name
        self.contents = contents
        self.parent = parent
        self.sum = 0

    def __str__(self) -> str:
        return self.dir_name

def make_sum(node):

    sum = 0
    for c in node.contents:
        if type(c) != Node:
            sum += c[0]
        else:
            sum += make_sum(c)

    node.sum = sum
    return sum

def find_sums(node):

    current_sum = 0
    for c in node.contents:
        if type(c) == Node:
            if c.sum < 100000:
                current_sum += c.sum
            current_sum += find_sums(c)
            
    return current_sum

def find_min(node, remaining):

    stack = [node]
    sums = [node.sum]
    while stack:
        node = stack.pop()
        for c in node.contents:
            if type(c) == Node:
                sums.append(c.sum)
                stack.append(c)
    sums.sort()
    for s in sums:
        if s > remaining:
            return s
            


def main(data):

    main_node = Node("/", [], None)
    line = 1
    while line <= len(data)-1:
        d = data[line].split(" ")
        if d[1] == "cd":
            for node in main_node.contents:
                if type(node) == Node and node.dir_name == d[-1]:
                    main_node = node
                    break
            
        if d[-1] == "ls":
            line += 1
            contents = []
            s = 0
            while data[line][0] != "$":
                d = data[line].split(" ")
                if d[0] == "dir":
                    node = Node(d[-1], [], main_node)
                    contents.append(node)
                else:
                    contents.append((int(d[0]),d[1]))
                line += 1
                if line == len(data):
                    break
            main_node.contents = contents
            main_node.sum = s
            continue
            
                
        if d[-1] == "..":
            main_node = main_node.parent

        line +=1

    while main_node.parent != None:
        main_node = main_node.parent

    return main_node

if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().split("\n")

    node = main(data)
    make_sum(node)
    sum = find_sums(node)
    print(sum)
    free_space = 70000000 - node.sum
    remaining = 30000000 - free_space
    sum = find_min(node, remaining)
    print(sum)