file = open('input.txt', 'r')
input = file.readlines()
file.close()

sum = 0
for line in input:
  line = line.strip("\n")
  first = line.split(",")[0]
  second = line.split(",")[1]

  # Check if first half is fully contained in the second half
  if int(first.split("-")[0]) >= int(second.split("-")[0]) and int(first.split("-")[1]) <= int(second.split("-")[1]):
    sum += 1
  # Check if second half is fully contained in the first half
  elif int(second.split("-")[0]) >= int(first.split("-")[0]) and int(second.split("-")[1]) <= int(first.split("-")[1]):
    sum += 1

print(sum)