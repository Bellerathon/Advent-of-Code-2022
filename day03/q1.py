file = open('input.txt', 'r')
input = file.readlines()
file.close()

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
sum = 0
for line in input:
  line = line.strip("\n")

  # Split line in half evenly
  first_half = line[:int(len(line)/2)]
  second_half = line[int(len(line)/2):]

  for char1 in first_half:
    # Check if a char in first half appears in second half
    if char1 in second_half:
      if char1.isupper():
        sum += alpha.index(char1.lower()) + 27
      else:
        sum += alpha.index(char1) + 1
      break

print(sum)