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
