def get_int(prompt):
  while True:
    try:
        return int(input(prompt))
    except ValueError:
        pass


scores = []

for i in range(3):
    x = get_int("what's x: ")
    scores.append(x)

average = sum(scores) / len(scores)
print(f"Average: {average:.2f}")
