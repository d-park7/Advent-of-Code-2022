from anytree import Node, RenderTree
from copy import deepcopy

LIMIT = 100000
TOTAL_DISK_SPACE = 70000000
MIN_UNUSED_SPACE = 30000000

commands = []
with open('input.txt', 'rt') as file:
    for line in file.read().splitlines():
        # After checking input, ignore line 1, and filer out ls and dir statements
        #  Can just create a directory when (cd <dir>)
        if "$ cd /" in line or "$ ls" in line or "dir " in line:
            continue
        else:
            commands.append(line)

# Create root node
root = Node(name='root', parent=None, files=dict(), size=0)
node = root

for i in range(len(commands)):
    cmd = commands[i]

    # Navigate up, or go down into directory
    if "$ cd" in cmd:
        dir = str(cmd).replace("$ cd ", "")
        if dir == '..':
            node = node.parent
        else:
            # Create node when going down into a directory (All dirs will be unique based on input)
            next_dir = Node(name=dir, parent=node, files=dict(), size=0)
            node = next_dir

    # Gather file size
    else:
        tok = cmd.split(' ')
        file_size = int(tok[0])
        file_name = tok[1]
        node.files[file_name] = file_size
        node.size += file_size



root_copy = deepcopy(root)

total_sizes = []
all_sizes = []

# Add leaves upward to find total size
while len(root.children) > 0:
    for node in root.leaves:
        # Check if any leaves are less than 100000
        if node.size <= LIMIT:
            total_sizes.append(node.size)
        
        # Add child node size to parent, then detach
        node.parent.size += node.size
        node.parent = None

        # Add node size at all points for reference (part 2)
        all_sizes.append(node.size)
    

print("Part 1:", sum(total_sizes))


FREE_SPACE = TOTAL_DISK_SPACE - root.size
SPACE_TO_DELETE = MIN_UNUSED_SPACE - FREE_SPACE
del_dir_size = -1

# Sort all node sizes and find first one (smallest)
all_sizes = sorted(all_sizes)
for size in all_sizes:
    if size >= SPACE_TO_DELETE:
        del_dir_size = size
        break

print("Part 2:", del_dir_size)



