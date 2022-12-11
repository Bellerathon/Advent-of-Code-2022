file = open('input.txt', 'r')
input = file.readlines()
file.close()

cycles = 0
register = 1
# Target cycles are 40,80,120,160,200,240
target = 40

# Each target cycle from previous to next e.g 1 -> 40, 41 -> 80 is a CRT line where each index is a pixel as represented in the array below of length 40
# 3 "#" sprites populate this line where the index of the centre "#" equals the register value, refreshed every time the register changes
sprite_position = ["#","#","#",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."]
current = ""

for line in input:
  line = line.strip("\n")
  # There's only 2 commands so if not noop its addx
  if line != "noop":
    value = line.split(" ")[1]
    j = 0
    # Addx commands need 2 cycles to execute
    while j < 2:
      # If target is reached during addx execution then print the current sprite positions
      if cycles == target:
        print(current)
        cycles = 0
        current = ""
      # If a "#" exists in the index of the current cycle then add a "#" to the CRT line else an empty space
      if sprite_position[cycles] == "#":
        current += "#"
      else:
        current += " "
      cycles += 1
      j += 1
      # If target is reached after addx execution then print the current sprite positions
      if cycles == target:
        print(current)
        cycles = 0
        current = ""
    # At this point the register has changed so replace the current sprite positions with "." and place 3 "#" in the indexes of the current register value
    sprite_position[register] = "."
    sprite_position[register - 1] = "."
    sprite_position[register + 1] = "."
    register += int(value)
    sprite_position[register] = "#"
    sprite_position[register - 1] = "#"
    sprite_position[register + 1] = "#"
  # Command is noop
  else:
    # If target is reached during noop execution then print the current sprite positions
    if cycles == target:
      print(current)
      cycles = 0
      current = ""
    # If a "#" exists in the index of the current cycle then add a "#" to the CRT line else an empty space
    if sprite_position[cycles] == "#":
        current += "#"
    else:
      current += " "
    
    # Noop command only needs one cycle to execute
    cycles += 1

# Result after each print statement line combines into an image PLGFKAZG (theres an off-by-one bug somewhere but still readable through deduction as they must be capital letters)

###  #     ##  #### #  #  ##  ####  ##  
#  # #    #  # #    # #  #  #    # #  # 
#  # #    #    ###  ##   #  #   #  #    
###  #    # ## #    # #  ####  #   # ## 
#    #    #  # #    # #  #  # #    #  # 