# Need this as a weird bug where appending a list to a list didnt work: https://stackoverflow.com/questions/69069838/weird-list-append-bug-in-python
from copy import deepcopy

file = open('input.txt', 'r')
input = file.readlines()
file.close()

# Starting positions
head = [0, 0]
tail = [0, 0]
# Keep  record of each position the tail is in
positions = []
for line in input:
  line = line.strip("\n")
  direction, distance = line.split(" ")
  # Move head first in direction and distance specified in input line
  for i in range(int(distance)):
    if direction == "R":
      head[1] += 1
    elif direction == "L":
      head[1] -= 1
    elif direction == "U":
      head[0] -= 1
    elif direction == "D":  
      head[0] += 1
    
    # Move tail after head
    # If tail is not in the same row and not in the same column and is more than one space away it moves diagonally
    if (head[1] != tail[1] and head[0] != tail[0]) and (abs(tail[1] - head[1]) > 1 or abs(tail[0] - head[0]) > 1):
      # Tail is below head so move it diagonally directly below head
      if tail[0] - head[0] > 1:
        tail[0] = head[0] + 1
        tail[1] = head[1]
        if tail not in positions: positions.append(deepcopy(tail))
      # Tail is above head so move it diagonally directly above head
      elif head[0] - tail[0] > 1:
        tail[0] = head[0] - 1
        tail[1] = head[1]
        if tail not in positions: positions.append(deepcopy(tail))
      # Tail is left of head so move it diagonally directly to its left
      elif head[1] - tail[1] > 1:
        tail[1] = head[1] - 1
        tail[0] = head[0]
        if tail not in positions: positions.append(deepcopy(tail))
      # Tail is right of head so move it diagonally directly to its right
      elif tail[1] - head[1] > 1:
        tail[1] = head[1] + 1
        tail[0] = head[0]
        if tail not in positions: positions.append(deepcopy(tail))
    # Tail is 'touching' head so just move it normaly
    else:
      # Move tail one column to the left
      if head[1] - tail[1] > 1:
        tail[1] += 1
        if tail not in positions: positions.append(deepcopy(tail))
      # Move tail one column to the right
      elif tail[1] - head[1] > 1:
        tail[1] -= 1
        if tail not in positions: positions.append(deepcopy(tail))
      # Move tail one row up
      elif tail[0] - head[0] > 1:
        tail[0] -= 1
        if tail not in positions: positions.append(deepcopy(tail))
      # Move tail one column down
      elif head[0] - tail[0] > 1:
        tail[0] += 1
        if tail not in positions: positions.append(deepcopy(tail))

# Only unique position will be in the array, get its length
print(len(positions))
