# --- Part Two ---
# You're worried you might not ever get your items back. So worried, in fact, that your relief that a monkey's inspection didn't damage an item no longer causes your worry level to be divided by three.

# Unfortunately, that relief was all that was keeping your worry levels from reaching ridiculous levels. You'll need to find another way to keep your worry levels manageable.

# At this rate, you might be putting up with these monkeys for a very long time - possibly 10000 rounds!

# With these new rules, you can still figure out the monkey business after 10000 rounds. Using the same example above:

# == After round 1 ==
# Monkey 0 inspected items 2 times.
# Monkey 1 inspected items 4 times.
# Monkey 2 inspected items 3 times.
# Monkey 3 inspected items 6 times.

# == After round 20 ==
# Monkey 0 inspected items 99 times.
# Monkey 1 inspected items 97 times.
# Monkey 2 inspected items 8 times.
# Monkey 3 inspected items 103 times.

# == After round 1000 ==
# Monkey 0 inspected items 5204 times.
# Monkey 1 inspected items 4792 times.
# Monkey 2 inspected items 199 times.
# Monkey 3 inspected items 5192 times.

# == After round 2000 ==
# Monkey 0 inspected items 10419 times.
# Monkey 1 inspected items 9577 times.
# Monkey 2 inspected items 392 times.
# Monkey 3 inspected items 10391 times.

# == After round 3000 ==
# Monkey 0 inspected items 15638 times.
# Monkey 1 inspected items 14358 times.
# Monkey 2 inspected items 587 times.
# Monkey 3 inspected items 15593 times.

# == After round 4000 ==
# Monkey 0 inspected items 20858 times.
# Monkey 1 inspected items 19138 times.
# Monkey 2 inspected items 780 times.
# Monkey 3 inspected items 20797 times.

# == After round 5000 ==
# Monkey 0 inspected items 26075 times.
# Monkey 1 inspected items 23921 times.
# Monkey 2 inspected items 974 times.
# Monkey 3 inspected items 26000 times.

# == After round 6000 ==
# Monkey 0 inspected items 31294 times.
# Monkey 1 inspected items 28702 times.
# Monkey 2 inspected items 1165 times.
# Monkey 3 inspected items 31204 times.

# == After round 7000 ==
# Monkey 0 inspected items 36508 times.
# Monkey 1 inspected items 33488 times.
# Monkey 2 inspected items 1360 times.
# Monkey 3 inspected items 36400 times.

# == After round 8000 ==
# Monkey 0 inspected items 41728 times.
# Monkey 1 inspected items 38268 times.
# Monkey 2 inspected items 1553 times.
# Monkey 3 inspected items 41606 times.

# == After round 9000 ==
# Monkey 0 inspected items 46945 times.
# Monkey 1 inspected items 43051 times.
# Monkey 2 inspected items 1746 times.
# Monkey 3 inspected items 46807 times.

# == After round 10000 ==
# Monkey 0 inspected items 52166 times.
# Monkey 1 inspected items 47830 times.
# Monkey 2 inspected items 1938 times.
# Monkey 3 inspected items 52013 times.
# After 10000 rounds, the two most active monkeys inspected items 52166 and 52013 times. Multiplying these together, the level of monkey business in this situation is now 2713310158.

# Worry levels are no longer divided by three after each item is inspected; you'll need to find another way to keep your worry levels manageable. Starting again from the initial state in your puzzle input, what is the level of monkey business after 10000 rounds?

# Your puzzle answer was 15048718170.

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
        # Divides worry by the divisble number above to reduce it
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