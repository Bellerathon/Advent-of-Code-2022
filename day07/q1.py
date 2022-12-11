file = open('input.txt', 'r')
input = file.readlines()
file.close()

dirs = {} 
current_dir = ""
# Parse input and keep track of current directory like a terminal where each directory path is stored as a key in a dict and it value is a list of files at that path location
# e.g cd hello -> /hello, cd world -> /hello/world, cd .. -> /hello
# e.g '/fhhwv/bjml/zzvs/vmbrt': ['194547', '54334', '/fhhwv/bjml/cwghv']
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

# Get size of a sub-folder recursively
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
  # Sum of directories without counting the sub-folders
  for value in values:
    if value.isdigit():
      sum += int(value)
    else:
      dirs_present = True

  # If a directory size is less than limit with only the files counted then proceed to count with the folders included too, else continue iteration
  if sum <= 100000 and dirs_present == True:
    sum = 0
    for value in values:
      # If a file
      if value.isdigit():
        sum += int(value)
      # If a directory
      else:
        # Get size of a sub-folder
        sum += get_sum(value)
    if sum <= 100000:
      valid.append(int(sum))
  elif sum <= 100000 and dirs_present == False:
    if sum <= 100000:
      valid.append(int(sum))
  else:
    if sum <= 100000:
      valid.append(int(sum))

# Sum of all directories sized <= 100,000
sum = 0
for num in valid:
  sum += int(num)

print(sum)