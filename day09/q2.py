# Need this as a weird bug where appending a list to a list didnt work: https://stackoverflow.com/questions/69069838/weird-list-append-bug-in-python
from copy import deepcopy

file = open('input.txt', 'r')
input = file.readlines()
file.close()

# Starting positions, 10 knots: 1 head and 9 knots
knots = [[0, 0], [0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0]]
# Keep  record of each position the tail is in
positions = []
for line in input:
  line = line.strip("\n")
  direction, distance = line.split(" ")
  # Move head first in direction and distance specified in input line, head is index 0 of knots array
  for i in range(int(distance)):
    if direction == "R":   
      knots[0][1] += 1
    elif direction == "L":
      knots[0][1] -= 1
    elif direction == "U":
      knots[0][0] -= 1
    elif direction == "D":
      knots[0][0] += 1
    # For every not after head, they move one after the other, using the previous' position to determine their position
    for j in range(1, len(knots)):
      # Move knot after head
      # If knot is not in the same row and not in the same column and is more than one space away from previous knot it moves diagonally
      if (knots[j-1][1] != knots[j][1] and knots[j-1][0] != knots[j][0]) and (abs(knots[j][1] - knots[j-1][1]) > 1 or abs(knots[j][0] - knots[j-1][0]) > 1):      
        # knots[j] below
        if knots[j][0] - knots[j-1][0] > 1:
          knots[j][0] = knots[j-1][0] + 1
          knots[j][1] = knots[j-1][1]
          if j == 9 and knots[j] not in positions: positions.append(deepcopy(knots[j]))
        # knots[j] above
        elif knots[j-1][0] - knots[j][0] > 1:
          knots[j][0] = knots[j-1][0] - 1
          knots[j][1] = knots[j-1][1]
          if j == 9 and knots[j] not in positions: positions.append(deepcopy(knots[j]))
        # knots[j] left
        elif knots[j-1][1] - knots[j][1] > 1:
          knots[j][1] = knots[j-1][1] - 1
          knots[j][0] = knots[j-1][0]
          if j == 9 and knots[j] not in positions: positions.append(deepcopy(knots[j]))
        # knots[j] right
        elif knots[j][1] - knots[j-1][1] > 1:
          knots[j][1] = knots[j-1][1] + 1
          knots[j][0] = knots[j-1][0]
          if j == 9 and knots[j] not in positions: positions.append(deepcopy(knots[j]))
      else:
        # Move knot right one
        if knots[j-1][1] - knots[j][1] > 1:
          knots[j][1] += 1
          if j == 9 and knots[j] not in positions: positions.append(deepcopy(knots[j]))
        # Move knot left one
        elif knots[j][1] - knots[j-1][1] > 1:
          knots[j][1] -= 1
          if j == 9 and knots[j] not in positions: positions.append(deepcopy(knots[j]))
        # Move knot up one
        elif knots[j][0] - knots[j-1][0] > 1:
          knots[j][0] -= 1
          if j == 9 and knots[j] not in positions: positions.append(deepcopy(knots[j]))
        # Move knot down one
        elif knots[j-1][0] - knots[j][0] > 1:
          knots[j][0] += 1
          if j == 9 and knots[j] not in positions: positions.append(deepcopy(knots[j]))

print(len(positions))