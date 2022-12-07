# --- Day 7: No Space Left On Device ---
# You can hear birds chirping and raindrops hitting leaves as the expedition proceeds. Occasionally, you can even hear much louder sounds in the distance; how big do the animals get out here, anyway?

# The device the Elves gave you has problems with more than just its communication system. You try to run a system update:

# $ system-update --please --pretty-please-with-sugar-on-top
# Error: No space left on device
# Perhaps you can delete some files to make space for the update?

# You browse around the filesystem to assess the situation and save the resulting terminal output (your puzzle input). For example:

# $ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k
# The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files). The outermost directory is called /. You can navigate around the filesystem, moving into or out of directories and listing the contents of the directory you're currently in.

# Within the terminal output, lines that begin with $ are commands you executed, very much like some modern computers:

# cd means change directory. This changes which directory is the current directory, but the specific result depends on the argument:
# cd x moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
# cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.
# cd / switches the current directory to the outermost directory, /.
# ls means list. It prints out all of the files and directories immediately contained by the current directory:
# 123 abc means that the current directory contains a file named abc with size 123.
# dir xyz means that the current directory contains a directory named xyz.
# Given the commands and output in the example above, you can determine that the filesystem looks visually like this:

# - / (dir)
#   - a (dir)
#     - e (dir)
#       - i (file, size=584)
#     - f (file, size=29116)
#     - g (file, size=2557)
#     - h.lst (file, size=62596)
#   - b.txt (file, size=14848514)
#   - c.dat (file, size=8504156)
#   - d (dir)
#     - j (file, size=4060174)
#     - d.log (file, size=8033020)
#     - d.ext (file, size=5626152)
#     - k (file, size=7214296)

# Here, there are four directories: / (the outermost directory), a and d (which are in /), and e (which is in a). These directories also contain files of various sizes.

# Since the disk is full, your first step should probably be to find directories that are good candidates for deletion. To do this, you need to determine the total size of each directory. The total size of a directory is the sum of the sizes of the files it contains, directly or indirectly. (Directories themselves do not count as having any intrinsic size.)

# The total sizes of the directories above can be found as follows:

# The total size of directory e is 584 because it contains a single file i of size 584 and no other directories.
# The directory a has total size 94853 because it contains files f (size 29116), g (size 2557), and h.lst (size 62596), plus file i indirectly (a contains e which contains i).
# Directory d has total size 24933642.
# As the outermost directory, / contains every file. Its total size is 48381165, the sum of the size of every file.
# To begin, find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes. In the example above, these directories are a and e; the sum of their total sizes is 95437 (94853 + 584). (As in this example, this process can count files more than once!)

# Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?

# Your puzzle answer was 2104783.

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
  # Folder contains a sub-directory so save its path to the dict
  if line[0] == "dir":
    if current_dir in dirs:
      dirs[current_dir].append(current_dir + "/" + line[1])
    else:
      dirs[current_dir] = [current_dir + "/" + line[1]]

# Get size of a sub-directory recursively
def get_sum(key):
  values = dirs[key]
  sum = 0
  for value in values:
    # Only sums files
    if value.isdigit():
      sum += int(value)

  # If just file sizes haven't breached limit then include sizes of folders
  if sum <= 100000:
    for value in values:
      if not value.isdigit():
        sum += get_sum(value)
    return sum

  return 99999999

# Calculate the total size of a folder
valid = []
for key in dirs:
  values = dirs[key]
  sum = 0
  dirs_present = False
  # Sum of directories without counting the sub-directories
  for value in values:
    if value.isdigit():
      sum += int(value)
    else:
      dirs_present = True

  # If a directory size is less than limit with only the files counted then proceed to count with the subdirectories included too else continue iteration
  if sum <= 100000 and dirs_present == True:
    sum = 0
    for value in values:
      # If a file
      if value.isdigit():
        sum += int(value)
      # If a directory
      else:
        # Get size of a sub-directory
        sum += get_sum(value)
    if sum <= 100000:
      valid.append(int(sum))
  elif sum <= 100000 and dirs_present == False:
    if sum <= 100000:
      valid.append(int(sum))
  else:
    if sum <= 100000:
      valid.append(int(sum))

# Sum of all directory size <= 100,000
sum = 0
for num in valid:
  sum += int(num)

print(sum)