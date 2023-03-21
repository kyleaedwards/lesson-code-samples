from lib import get_number

num = get_number()
numbers = []

# Loop forever until the user enters a 0.
while num != 0:
  # If the number is valid, add it to the list.
  if num is not None:
    numbers.append(num)
  num = get_number()

# The sum() and len() functions both can take lists as arguments
# and calculate the total and the length. Note that len() can
# return the length of other data types like strings and
# dictionaries (in Python, they're often called "dicts").
total = sum(numbers)
length = len(numbers)

# Since we can't divide by 0, we first check and then print the
# results.
if length > 0:
  print("The average for " + str(numbers) + " is " + str(total / length))
else:
  print("Next time add some numbers")
