
from re import sub
from clipboard import paste

# Import clipboard to variable
text = paste()

# Split it to lines
splitlines = text.splitlines(True)

# Sort the lines
splitlines.lower()

# List comprehension with Regex
out = [sub(r'\r|\n|^\s+', '', line) for line in splitlines]

# Print the output
print(*out, sep = '\n')
