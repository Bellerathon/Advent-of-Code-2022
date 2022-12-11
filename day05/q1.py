file = open('input.txt', 'r')
input = file.readlines()
file.close()

stacks = [["N", "R", "G", "P"], ["J", "T", "B", "L", "F", "G", "D", "C"], ["M", "S", "V"], ["L", "S", "R", "C", "Z", "P"], ["P", "S", "L", "V", "C", "W", "D", "Q"], ["C", "T", "N", "W", "D", "M", "S"], ["H", "D", "G", "W", "P"], ["Z", "L", "P", "H", "S", "C", "M", "V"], ["R", "P", "F", "L", "W", "G", "Z"]]

for line in input:
  line = line.strip("\n")
  words = line.split()

  # Only keep the numbers present in the line
  numbers = []
  for word in words:
    try:
      numbers.append(int(word))
    except ValueError:
      pass
  
  # Assign them to there respective variables
  num_move = numbers[0]
  from_stack = numbers[1]
  to_stack = numbers[2]

  # Take value from end of one stack and appending to the end of a target list
  for i in range(num_move):
    stacks[to_stack - 1].append(stacks[from_stack - 1].pop())

# Get the value in the last index of each list
final_arrangment = ""
for i in range(len(stacks)):
  final_arrangment += str(stacks[i].pop())

print(final_arrangment)

  
  