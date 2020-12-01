import json, sys, os

#Declaring Variables
spaces = ""
singlefile = True
jsonfiles = []

### This Area is filtering through given arguments and checking file validity. ###
#Did they specify what they wanted modified?
try:
    file = sys.argv[1]
except IndexError as err:
    print("Please define a file to modify.")
    sys.exit()
else:
    jsonfiles.append(file)

#Function to get list of valid files in the directory if they seleced "all".
def filter_files():
    for file in jsonfiles:
        if ".json" not in file:
            jsonfiles.remove(file)

#Makes sure it's a .json file, or they chose all files.
if ".json" not in file:
    if file == "all":
        jsonfiles = os.listdir(".")
        filter_files()
        print("Selecting all files in this directory ending in .json to edit.")
        response = input("Are you sure you want to continue? (Y/N): ")
        if response.lower() == "y":
            print("Continuing...")
            singlefile = False
        else:
            sys.exit()
    else:
        print("Error. Not a JSON file. This program only accepts files appended with .json.")
        sys.exit()

#Function to check if the file is technically a valid json file. Will not be called if "all" files are selected.
def try_json():
    try:
        json.loads(data)
    except TypeError as err:
        print("Error: Please choose a valid JSON file. If you wish to bypass this, add \'bypass\' as an argument after the file.")
        sys.exit()

### This area does a final JSON validity check, then starts searching for missing instances of TPYE. ###
for file in jsonfiles:
    newlines = []
    index = []
    inside = False

    with open(file, 'r') as data:
        if singlefile:
            try:
                file = sys.argv[2]
            except IndexError as err:
                try_json()
            else:
                if sys.argv[2] != "bypass":
                    try_json()
                else:
                    print("Bypassing any possible \'Invalid JSON\' errors...")

        for line in data:
            newlines.append(line)
            if ('\"count\"' in line) & ('{' in line) & (':' in line):
                inside = True
            if inside:
                if '\"type\"' in line:
                    inside = False
                if '}' in line:
                    index.append(len(newlines) - 3)
                    inside = False

#This inserts the new "type": "minecraft:uniform" line into the list of lines, with correct indentation.
    index.reverse()
    for item in index:
        count = 0
        for letter in newlines[item]:
            if letter == " ":
                count += 1
        spaces = " " * (count - 1)
        newlines.insert(item, f'{spaces}\"type\": \"minecraft:uniform\",\n')

#Finally, writes the new lines into given json file, replacing the old text.
    with open(file, 'w') as f_out:
        f_out.writelines(newlines)
        print("Success!")
        if len(index) != 0:
            print(f"Added a TYPE for {len(index)} instances of COUNT in {file}.")
        else:
            if singlefile:
                print("No changes were to be made.")


###OLD CODE###
#count = []
#path = []

#def find_count(current):
#    count.append(0)
#    level = count[len(count)-1]
#
#    if type(current) == dict:
#        print(f'\n{current}\n')
#        for k, v in current.items():
#            if isinstance(k, str):
#                if (k == "min") | (k == "max"):
#                    #current["type"] = "minecraft:uniform"
#                    print('')
#        for item in current.items():
#            find_count(item)#
#
#    if type(current) == list:
#        for item in current:
#            find_count(item)
#
#    if type(current) == tuple:
#        count[level] = 0
#        while count[level] <= len(current) - 1:
#            if type(current[count[level]]) == str:
#                count[level] += 1
#                continue
#            else:
#                find_count(current[count[level]])
#            count[level] += 1
#
#    count.pop(len(count)-1)

#for item in data.items():
#        if type(data) == dict:
#            find_count(item)
#        if type(data) == list:
#            for item in data:
#                find_count(item)
#        if type(data) == tuple:
#            if data[0] == "type":
#                print("Found a type!\n\n")
#            else:
#                find_count(item)