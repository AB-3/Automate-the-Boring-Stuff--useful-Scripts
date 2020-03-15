#! python3
#mcb.pwy - saves and loads pecies of text to the clipboard.
"""
Usage:py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
 py.exe mcb.pyw list - Loads all keywords to clipboard.
"""
import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#saves clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    mcbShelf.pop(sys.argv[2])
elif len(sys.argv) == 2:
    #list keywords and load content.
    if sys.argv[1].lower == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    if sys.argv[1].lower == 'delall':
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])


mcbShelf.close()
