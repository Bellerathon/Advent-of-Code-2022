
file = open('input.txt', 'r')
input = file.readlines()
file.close()

cycles = 0
register = 1
# Target cycles are 20,60,100,140,180,220
target = 20
candidates = []
sum = 0
for line in input:
  line = line.strip("\n")
  # There's only 2 commands so if not noop its addx
  if line != "noop":
    # Get addx value
    value = line.split(" ")[1]
    j = 0
    # Addx commands need 2 cycles to execute
    while j < 2:
      cycles += 1
      # If target is reached during addx execution then record the current register
      if cycles == target:
        candidates.append(register)
      j += 1
      # If target is reached after addx execution then record the current register
      if cycles == target:
        candidates.append(register)
    register += int(value)
  # Noop commnad does nothing but consumes a cycle
  else:
    cycles += 1

  # Keep whichever register was recorded first and mulitply by target cycle value to find signal strength
  if len(candidates) > 0:
    sum += candidates[0] * target
    target += 40
    candidates = []

print(sum)
