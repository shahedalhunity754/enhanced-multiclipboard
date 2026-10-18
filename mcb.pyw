#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword>      - Loads text associated with keyword to clipboard.
#        py.exe mcb.pyw list           - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete <keyword>- Deletes a keyword from the shelf.
#        py.exe mcb.pyw delete         - Deletes all keywords from the shelf.

import sys 
import shelve
import pyperclip

mcb_shelf = shelve.open('mcb')

if len(sys.argv) == 3:
    command = sys.argv[1].lower()
    keyword = sys.argv[2]

    if command == 'save':
        mcb_shelf[keyword] = pyperclip.paste()
    elif command == 'delete':
        if keyword in mcb_shelf:
            del mcb_shelf[keyword]

elif len(sys.argv) == 2:
    command = sys.argv[1].lower()

    if command == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))

    elif command == 'delete':
        mcb_shelf.clear()
    elif command in mcb_shelf:
        pyperclip.copy(mcb_shelf[command])


mcb_shelf.close()
