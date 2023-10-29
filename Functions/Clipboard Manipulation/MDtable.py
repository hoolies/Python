"""This allow you to copy rows and columns from a spreadsheet and creates a markdown table"""
from re import sub
from clipboard import paste

def main():
    """Main Function"""
    markup = []
    
    text = paste()
    
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
        replace = sub(r'\t', " | ", line)
        # Remove new lines and enter
        line = sub(r'\r', '', replace)
        replace = sub(r'\n', '', line)
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
if __name__ == "__main__":
    main()
