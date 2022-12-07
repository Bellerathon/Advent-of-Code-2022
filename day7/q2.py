# --- Part Two ---
# Now, you're ready to choose a directory to delete.

# The total disk space available to the filesystem is 70000000. To run the update, you need unused space of at least 30000000. You need to find a directory you can delete that will free up enough space to run the update.

# In the example above, the total size of the outermost directory (and thus the total amount of used space) is 48381165; this means that the size of the unused space must currently be 21618835, which isn't quite the 30000000 required by the update. Therefore, the update still requires a directory with total size of at least 8381165 to be deleted before it can run.

# To achieve this, you have the following options:

# Delete directory e, which would increase unused space by 584.
# Delete directory a, which would increase unused space by 94853.
# Delete directory d, which would increase unused space by 24933642.
# Delete directory /, which would increase unused space by 48381165.
# Directories e and a are both too small; deleting them would not free up enough space. However, directories d and / are both big enough! Between these, choose the smallest: d, increasing unused space by 24933642.

# Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?

# Your puzzle answer was 5883165.

file = open('input.txt', 'r')
input = file.readlines()
file.close()

dirs = {}
current_dir = ""
for line in input:
  line = line.strip("\n")
  line = line.split(" ")
  if line[0] == "$":
    if line[1] == "cd":
      if line[2] == "..":
        current_dir = current_dir.rsplit('/', 1)[0]
        print(current_dir)
      else:
        current_dir += str("/" + line[2])
        print(current_dir)
  if line[0].isdigit():
    if current_dir in dirs:
      dirs[current_dir].append(line[0])
    else:
      dirs[current_dir] = [line[0]]
  if line[0] == "dir":
    if current_dir in dirs:
      dirs[current_dir].append(current_dir + "/" + line[1])
    else:
      dirs[current_dir] = [current_dir + "/" + line[1]]

def get_sum(key):
  values = dirs[key]
  sum = 0
  for value in values:
    if value.isdigit():
      sum += int(value)
    else:
      sum += get_sum(value)

  return sum

count = 0
sums = []
for key in dirs:
  values = dirs[key]
  sum = 0
  non_digits = False
  for value in values:
    gg = value
    if value.isdigit():
      sum += int(value)
    else:
      non_digits = True

    sum = 0
    for value in values:
      if value.isdigit():
        sum += int(value)
      else:
        found = get_sum(value)
        sum += found
  sums.append(sum)

max = 70000000
current = get_sum("//")
diff = max - current
need = 30000000 - diff

sums.sort()

# Find the min directory size that needs to be removed by sorting list first then iterating low -> high
for sum in sums:
  if sum >= need:
    print(sum)
    break