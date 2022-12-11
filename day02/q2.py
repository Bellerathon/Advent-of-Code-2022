file = open('input.txt', 'r')
input = file.readlines()
file.close()

o_rock = "A"
o_paper = "B"
o_scissor = "C"

rock = 1
paper = 2
scissor = 3

win = "Z"
lose = "X"
draw = "Y"

lose_val = 0
tie_val = 3
win_val = 6

sum = 0
for line in input:
  line= line.strip("\n")
  opponent = line.split(" ")[0]
  result = line.split(" ")[1]
  
  if opponent == o_rock:
    if result == win:
      sum += (paper + win_val)
    if result == lose:
      sum += (scissor + lose_val)
    if result == draw:
      sum += (rock + tie_val)
  if opponent == o_scissor:
    if result == win:
      sum += (rock + win_val)
    if result == lose:
      sum += (paper + lose_val)
    if result == draw:
      sum += (scissor + tie_val)
  if opponent == o_paper:
    if result == win:
      sum += (scissor + win_val)
    if result == lose:
      sum += (rock + lose_val)
    if result == draw:
      sum += (paper + tie_val)
  
  
  
print(sum)