# --- Day 5: Supply Stacks ---
# The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

# The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

# The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

# They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
# In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

# Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

# [D]        
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

#         [Z]
#         [N]
#     [C] [D]
#     [M] [P]
#  1   2   3
# Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

#         [Z]
#         [N]
# [M]     [D]
# [C]     [P]
#  1   2   3
# Finally, one crate is moved from stack 1 to stack 2:

#         [Z]
#         [N]
#         [D]
# [C] [M] [P]
#  1   2   3
# The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

# After the rearrangement procedure completes, what crate ends up on top of each stack?

# Your puzzle answer was VPCDMSLWJ.

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

  
  