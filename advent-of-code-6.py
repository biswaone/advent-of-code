def find_marker(input_string):
  # Initialize variables to keep track of the most recent four characters
  # and the number of characters processed
  chars = []
  count = 0
  
  # Iterate through the input string
  for c in input_string:
    # Append the current character to the list of most recent characters
    chars.append(c)
    # Increment the count of characters processed
    count += 1
    # If there are more than four characters in the list, remove the oldest one
    if len(chars) > 4:
      chars.pop(0)
    # If the four most recent characters are all different, return the count
    if len(set(chars)) == 4:
      return count
  # If no marker was found, return -1
  return -1

def find_marker_2(input_string):
  # Initialize variables to keep track of the most recent 14 characters
  # and the number of characters processed
  chars = []
  count = 0
  
  # Iterate through the input string
  for c in input_string:
    # Append the current character to the list of most recent characters
    chars.append(c)
    # Increment the count of characters processed
    count += 1
    # If there are more than 14 characters in the list, remove the oldest one
    if len(chars) > 14:
      chars.pop(0)
    # If the 14 most recent characters are all different, return the count
    if len(set(chars)) == 14:
      return count
  # If no marker was found, return -1
  return -1

# Read the input from a text file
with open('advent-of-code-6.txt', 'r') as f:
  input_string = f.read()

# Find the first start-of-message marker
result_2 = find_marker_2(input_string)
print(result_2)


# Find the first start-of-packet marker
result_1 = find_marker(input_string)
print(result_1)
