file = open('q1_input.txt', 'r')
input = file.readlines()
file.close()

max = 0
elf = 0
count = 0
sum = 0
for line in input:
  # If line not empty then add value to group sum
  if line != "\n":
    sum += int(line.strip("\n"))
  else:
    # New line detected thus check sum of current group and then reset it for next group
    if sum > max:
      max = sum
      elf = count
    sum = 0
