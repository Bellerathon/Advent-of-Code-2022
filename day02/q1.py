file = open('input.txt', 'r')
input = file.readlines()
file.close()

o_rock = "A"
o_paper = "B"
o_scissor = "C"
y_rock = "X"
y_paper= "Y"
y_scissor = "Z"

rock = 1
paper = 2
scissor = 3

lose = 0
tie = 3
win = 6

sum = 0
for line in input:
  line= line.strip("\n")
  opponent = line.split(" ")[0]
  you = line.split(" ")[1]
  
  if you == y_rock:
    if opponent == o_paper:
      sum += (rock + lose)
    elif opponent == o_scissor:
      sum += (rock + win)
    elif opponent == o_rock:
      sum += (rock + tie)
  elif you == y_paper:
    if opponent == o_paper:
      sum += (paper + tie)
    elif opponent == o_scissor:
      sum += (paper + lose)
    elif opponent == o_rock:
      sum += (paper + win)
  elif you == y_scissor:
    if opponent == o_paper:
      sum += (scissor + win)
    elif opponent == o_scissor:
      sum += (scissor + tie)
    elif opponent == o_rock:
      sum += (scissor + lose)
  
print(sum)