file = open('input.txt', 'r') 
input = file.readlines()
file.close()

# Hard coded this parsing would be too time consuming
stacks = [["N", "R", "G", "P"], ["J", "T", "B", "L", "F", "G", "D", "C"], ["M", "S", "V"], ["L", "S", "R", "C", "Z", "P"], ["P", "S", "L", "V", "C", "W", "D", "Q"], ["C", "T", "N", "W", "D", "M", "S"], ["H", "D", "G", "W", "P"], ["Z", "L", "P", "H", "S", "C", "M", "V"], ["R", "P", "F", "L", "W", "G", "Z"]]

for line in input:
  line = line.strip("\n")
  words = line.split()

  numbers = []
  for word in words:
    try:
      numbers.append(int(word))
    except ValueError:
      pass

  num_move = numbers[0]
  from_stack = numbers[1]
  to_stack = numbers[2]
  
  numbers = []
  for i in range(num_move):
    numbers.append(stacks[from_stack - 1].pop())
  
  # Reverse the numbers that were popped of the target list to keep them in order they were put onto the target list
  numbers = numbers[::-1]
  for number in numbers:
    stacks[to_stack - 1].append(number)

final_arrangment = ""
for i in range(len(stacks)):
  final_arrangment += str(stacks[i].pop())

print(final_arrangment)