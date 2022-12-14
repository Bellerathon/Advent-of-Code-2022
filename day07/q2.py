file = open('input.txt', 'r')
input = file.readlines()
file.close()

dirs = {} 
current_dir = ""
# Parse input and keep track of current directory like a terminal where each directory path is stored as a key in a dict and it value is a list of files at that path location
# e.g cd hello -> /hello, cd world -> /hello/world, cd .. -> /hello
for line in input:
  line = line.strip("\n")
  line = line.split(" ")
  # A user command
  if line[0] == "$":
    if line[1] == "cd":
      # Reduce current directory by one level by removing everything after last "/" from it
      if line[2] == "..":
        current_dir = current_dir.rsplit('/', 1)[0]
      # Increase directory path by one level by concatinating "/{dir name}" to it
      else:
        current_dir += str("/" + line[2])
  # Folder contains a file
  if line[0].isdigit():
    # Add the file size to a directory path if one exists
    if current_dir in dirs:
      dirs[current_dir].append(line[0])
    # Create the path in the dict
    else:
      dirs[current_dir] = [line[0]]
  # Folder contains a sub-folder so save its path to the dict
  if line[0] == "dir":
    if current_dir in dirs:
      dirs[current_dir].append(current_dir + "/" + line[1])
    else:
      dirs[current_dir] = [current_dir + "/" + line[1]]

# Get sum of a directories files and folders recursively
def get_sum(key):
  values = dirs[key]
  sum = 0
  for value in values:
    if value.isdigit():
      sum += int(value)
    else:
      sum += get_sum(value)

  return sum

# Sum the size of all the files and folders in a directory
sums = []
for key in dirs:
  values = dirs[key]
  sum = 0
  for value in values:
    # A file
    if value.isdigit():
      sum += int(value)
    # A folder
    else:
      sum += get_sum(value)
  sums.append(sum)

max = 70000000
# Root directory contains all files and folder in system
current = get_sum("//")
diff = max - current
need = 30000000 - diff

sums.sort()

# Find the min directory size that needs to be removed by sorting list first then iterating low -> high
for sum in sums:
  if sum >= need:
    print(sum)
    break