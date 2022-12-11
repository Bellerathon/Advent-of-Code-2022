file = open('input.txt', 'r')
input = file.readlines()
file.close()

# Parse input file and store each monkey as an object with attributes
monkeys = {}
current_monkey = 0
divisibles = 1
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
        try:
          # Only the strings that are also numbers will be added to the array
          item = item.strip(",")
          monkeys[current_monkey]["items"].append(int(item))
        except ValueError:
          pass
    if line[0] == "Operation:":
      monkeys[current_monkey]["operation"] = line[4] + " " + line[5]
    if line[0] == "Test:":
      # This is the crux of part 2, I couldn't figure it out by myself. worry // 3 is removed in part 2 thus worry value becomes extremely large.
      # So large infact that after 200 rounds my computer was taking minutes to calculate a single round, and it needs to do 10,000 of them.
      # Needed a solution to reduce the worry value but can't change its value otherwise the result will be wrong. Thus use LCM (least common mulitple).
      # Found the idea on Reddit (https://www.reddit.com/r/adventofcode/comments/zih7gf/2022_day_11_part_2_what_does_it_mean_find_another/):
      # "You can devise a least common multiple by multiplying the "divisible by" numbers together and then modulo each new worry level by that number", see line below.
      divisibles *= int(line[3])
      monkeys[current_monkey]["test"] = line[3]
    if line[0] == "If" and line[1] == "true:":
      monkeys[current_monkey]["true"] = line[5]
    if line[0] == "If" and line[1] == "false:":
      monkeys[current_monkey]["false"] = line[5]
  else:
    monkey = {}

round = 0
worry = 0
while round < 10000:
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
        # Use the divisible number generated above as the modulo
        worry = worry % divisibles
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