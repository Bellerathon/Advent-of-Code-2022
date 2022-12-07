# --- Part Two ---
# By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

# To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

# In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

file = open('q1_input.txt', 'r')
input = file.readlines()
file.close()

sum = 0
calories_array = []
for line in input:
  if line != "\n":
    sum += int(line.strip("\n"))
  else:
    calories_array.append(sum)
    sum = 0

# Sort array high -> low then get first 3 (the 3 highest values)
calories_array.sort(reverse=True)
print(calories_array[0] + calories_array[1] + calories_array[2])