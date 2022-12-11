file = open('input.txt', 'r')
input = file.readlines()
file.close()

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
sum = 0
group = []
for line in input:
  line = line.strip("\n")
  group.append(line)
  if len(group) == 3:
    for char in group[0]:
      if char in group[1]:
        if char in group[2]:
          if char.isupper():
            sum += alpha.index(char.lower()) + 27
          else:
            sum += alpha.index(char) + 1
          group = []
          break

print(sum)