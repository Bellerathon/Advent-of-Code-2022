file = open('input.txt', 'r')
input = file.readlines()
file.close()

sum = 0
for line in input:
  line = line.strip("\n")
  first = line.split(",")[0]
  second = line.split(",")[1]

  # Fully contained
  if int(first.split("-")[0]) >= int(second.split("-")[0]) and int(first.split("-")[1]) <= int(second.split("-")[1]):
    sum += 1
  elif int(second.split("-")[0]) >= int(first.split("-")[0]) and int(second.split("-")[1]) <= int(first.split("-")[1]):
    sum += 1
  # Some overlap
  elif (int(second.split("-")[0]) >= int(first.split("-")[0])) and (int(second.split("-")[0]) <= int(first.split("-")[1])):
    sum +=1
  elif (int(first.split("-")[0]) >= int(second.split("-")[0])) and (int(first.split("-")[0]) <= int(second.split("-")[1])):
    sum +=1
    
print(sum)