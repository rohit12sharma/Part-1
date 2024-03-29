import csv
import re

print("Welcome to Language Conversion")

print('===================================================')

def conversion(user_string):
    user_string = user_string.split(" ")
    j = 0
    for _str in user_string:
        fileName = "lang.txt"        # Read Mode
        accessMode = "r"
        with open(fileName, accessMode) as myCSVfile:
            # Reading file as CSV with delimiter as "="
            dataFromFile = csv.reader(myCSVfile, delimiter="=")
            # Removing Special Characters.
            _str = re.sub('[^a-zA-Z0-9-_.]', '', _str)
            for row in dataFromFile:
                # Check if selected word matches short forms[LHS] in text file.
                if _str.upper() == row[0]:
                    # If match found replace it with its appropriate phrase in text file.
                    user_string[j] = row[1]
            myCSVfile.close()
        j = j + 1
    print(' '.join(user_string))
    print('===================================================')
    print('')

while True:
    print("Sample Script: TWODOLLARS were not needed  for CM to get TRIPLEA WTF . AFAIK the FAQ FWIW FYI get FC ROFL . BTW GG GN")
    print("Provide Input below or print exit or EXIT to end script")
    # Getting User String.
    user = input()
    # Keep Calling procedure until EXIT or exit keyword is encountered.
    if user.upper() == 'EXIT':
        print("Exiting Script")
        break
    conversion(user)
