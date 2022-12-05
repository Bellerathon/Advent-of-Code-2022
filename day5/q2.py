# --- Part Two ---
# As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

# Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

# The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

# Again considering the example above, the crates begin in the same configuration:

#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# Moving a single crate from stack 2 to stack 1 behaves the same as before:

# [D]        
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

#         [D]
#         [N]
#     [C] [Z]
#     [M] [P]
#  1   2   3
# Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

#         [D]
#         [N]
# [C]     [Z]
# [M]     [P]
#  1   2   3
# Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

#         [D]
#         [N]
#         [Z]
# [M] [C] [P]
#  1   2   3
# In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

# Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?

# Your puzzle answer was TPWCGNCCG. 

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
  
  numbers = numbers[::-1]
  for number in numbers:
    stacks[to_stack - 1].append(number)

final_arrangment = ""
for i in range(len(stacks)):
  final_arrangment += str(stacks[i].pop())

print(final_arrangment)