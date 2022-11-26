import re
import clipboard

# Import clipboard to variable
text = clipboard.paste()

# Split it to lines
splitlines = text.splitlines(True)

# Sort the lines
splitlines.sort()

# List comprehension with Regex
out = [re.sub(r'\r|\n|^\s+', '', line) for line in splitlines]

# Print the output
print(*out, sep = '\n')
