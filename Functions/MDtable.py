import re
import clipboard

markup = []

text = clipboard.paste()

splitlines = text.splitlines(True)

# Count how many columns to create
tabs = splitlines[0].count('\t') + 1

# Create the columns in Markdown
columns = ["-|" for i in range(tabs)]

#  Joun the columns with a space in between
column = ' '.join(columns)

# Create the Markdown
for i,line in enumerate(splitlines):
    # Replace the tabs with space pipe spcae
    replace = re.sub(r'\t', " | ", line)
    # Remove new lines and enter
    line = re.sub(r'\r', '', replace)
    replace = re.sub(r'\n', '', line)
    # Appends the changes to markdown
    markup.append(replace)
    # Add the columns
    if i == 0:
        markup.append(column)

# Finalize the output by adding new lines
out = '\n'.join(markup)

# Copy the output on the clipboard
# clipboard.copy(out)
print(out)
