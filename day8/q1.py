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
for row, line in enumerate(input):
  line = line.strip("\n")
  # if row is not top or bottom (on the borders)
  if row != 0 and row != len(rows) - 1:
    # For every column
    for column, height in enumerate(line):
      # if row is not left or right (on the borders)
      if column != 0 and column != len(line) - 1:

        # Everything before it in that row
        before = rows[row][:column]
        # Everything after it in that row
        after = rows[row][column + 1:]
        # Everthing above it in that column
        above = columns[column][row + 1:]
        # Everything below it in that column
        below = columns[column][:row]

        count = 0
        visible = 0
        # Check for each line of sight there are no trees are taller and blocking its visibility 
        if all(heights < height for heights in before):
          visible += 1
        if all(heights < height for heights in after):
          visible += 1
        if all(heights < height for heights in above):
          visible += 1
        if all(heights < height for heights in below):
          visible += 1
        
        # If at least one side can see the tree than at it to the total trees visible
        if visible > 0:
          total += 1

# Get the total number of trees surrounding the grid as these are all visible
total += (len(rows[0]) + len(rows[0]) + len(columns[0]) - 2 + len(columns[0]) - 2)

print(total)