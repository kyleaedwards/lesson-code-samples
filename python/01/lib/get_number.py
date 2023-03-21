# Prompt the user for input and try to read it as a number. If
# the string provided is not a number, return None.
def get_number():
  num = input("Input a number (enter 0 to quit): ")
  try:
    num = float(num)
  except:
    print(num + " is not a number, try again!")
    num = None
  return num
