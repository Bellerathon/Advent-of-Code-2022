file = open('input.txt', 'r')
input = file.readlines()
file.close()

# Each line in input file is a row
rows = []
for line in input:
  line = line.strip("\n")
  rows.append(line)

# To get the columns get the value at each row index for a column number. The value of a column is each of the values at the index of the corresponding row index
# E.g In a grid of 3 rows column[0] is row[0][0], row[1][0], and row[2][0]
columns = []
for i in range(len(rows[0])):
  column = ""
  for j in range(len(rows)):
    column += rows[j][i]
  columns.append(column)

# For every row
total = 0
distances_array = []
for row, line in enumerate(input):
  line = line.strip("\n")
  # if row is not top or bottom (on the borders)
  if row != 0 and row != len(rows) - 1:
    # for every column
    for column, height in enumerate(line):
      # if row is not left or right (on the borders)
      if column != 0 and column != len(line) - 1:

        # Everything before it in that row
        before = rows[row][:column]
        # Everything after it in that row
        after = rows[row][column+1:]
        # Everthing above it in that column
        below = columns[column][row + 1:]
        # Everything below it in that column
        above = columns[column][:row]

        distances = []
        # For each sightline direction count how many trees you can see before its blocked
        distance = 0
        # Array is indexed from border to target thus reverse so tree in first index is the one closest to viewer
        before = before[::-1]
        for heights in before:
          distance += 1
          if heights >= height:
            break
        distances.append(distance)

        distance = 0
        for heights in after:
          distance += 1
          if heights >= height:
            break
        distances.append(distance)

        distance = 0
        above = above[::-1]
        for heights in above:
          distance += 1
          if heights >= height:
            break
        distances.append(distance)

        distance = 0
        for heights in below:
          distance += 1
          if heights >= height:
            break
        distances.append(distance)

        distances_array.append(distances)

# Sum the total viewable distance from each sightlines from each tree to find and find which tree has the furthest total sightlines
distances_summed = []
for distance in distances_array:
  sum = 1
  for num in distance:
    sum *= num
  distances_summed.append(sum)

print(max(distances_summed))

