file = open('input.txt', 'r')
input = file.readlines()
file.close()

# Parse input file and store each monkey as an object with attributes
monkeys = {}
current_monkey = 0
for line in input:
  line = line.strip()
  if line:
    line = line.split(" ")
    # Intialise a monkey object
    if line[0] == "Monkey":
      current_monkey = int(line[1].strip(":"))
      monkeys[current_monkey] = {}
      monkeys[current_monkey]["items"] = []
      monkeys[current_monkey]["count"] = 0
    # Collect all the monkeys starting items
    if line[0] == "Starting":
      for item in line:
        # Only the strings that are also numbers will be added to the array
        try:
          item = item.strip(",")
          monkeys[current_monkey]["items"].append(int(item))
        except ValueError:
          pass
    if line[0] == "Operation:":
      monkeys[current_monkey]["operation"] = line[4] + " " + line[5]
    if line[0] == "Test:":
      monkeys[current_monkey]["test"] = line[3]
    if line[0] == "If" and line[1] == "true:":
      monkeys[current_monkey]["true"] = line[5]
    if line[0] == "If" and line[1] == "false:":
      monkeys[current_monkey]["false"] = line[5]
  else:
    monkey = {}

round = 0
worry = 0
while round < 20:
  # for every monkey object made above
  for monkey in monkeys.values():
    # Check monkey has any items else go to next monkey
    if len(monkey["items"]) > 0:
      # For every item monkey has inspect it
      for item in monkey["items"]:
        monkey["count"] += 1
        worry = int(item)
        symbol, term = monkey["operation"].split(" ")
        if term != "old":
          if symbol == "*":
            worry *= int(term)
          else:
            worry += int(term)
        else:
          if symbol == "*":
            worry *= worry
          else:
            worry += worry
        # Divides worry by three and rounds it down
        worry = worry // 3
        # Check if worry value is divisble by the test value
        if worry % int(monkey["test"]) == 0:
          # Send the item to the specified monkeys items
          monkeys[int(monkey["true"])]["items"].append(worry)
        else:
          monkeys[int(monkey["false"])]["items"].append(worry)
      # At this point each item has been inspected and past on so empty the monkeys items
      monkey["items"] = []
    else:
      pass

  round += 1

# Get each monkeys count
counts = []
for monkey in monkeys.values():
  counts.append(monkey["count"])

# Sort the counts high -> low
counts.sort(reverse=True)

# Take top 2 and mulitply them to find "level of monkey business"
print(counts[0] * counts[1])