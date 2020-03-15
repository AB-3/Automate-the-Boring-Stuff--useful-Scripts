#! python3
import re, pyperclip
#TODO: Create a regex object for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?                    #area code (optional)
(\s|-)                    #first separator
\d\d\d                    #first 3 digits
-                         #separator
\d\d\d\d                   #last 4 digits
((ext(\.)?\s)|(x)           #extension(optional)
(\d(2,5)))?
) ''', re.VERBOSE)

#TODO: create a regex object for email addresses
emailRegex = re.compile(r'''
[a-zA-z0-9_.+]+            #name part
@                           #@ symbol
[a-zA-z0-9_.+]+              #domain
''', re.VERBOSE)

#TODO: get text off clipboard
text = pyperclip.paste()
#TODO: extract email/phone from clipboard

extractedphone = phoneRegex.findall(text)

extractedemail = emailRegex.findall(text)

#print(extractedphone)
#print(extractedemail)

allPhonenumbers =[]
for phonenumber in extractedphone:
    allPhonenumbers.append(phonenumber[0])

results = '\n'.join(allPhonenumbers) +  '\n' + '\n'.join(extractedemail) #format in new lines
pyperclip.copy(results)
