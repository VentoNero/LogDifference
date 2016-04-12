#####################################################################
# Author: Michele Vinciguerra
# Date: 12/04/2016 - 22:32
# Description: script that calculates the differences between files 
# in a folder and creates a output file if any difference is found.
# This was mainly created to easily read through log files and 
# determine their differences.
# The system uses two tags, opening and closing, to get the list of 
# lines to compare.
#####################################################################

#!/usr/bin/python

import config
import sys
import os
import re
    
def ReadFile(path):
    with open(path, 'rb') as f:
        return f.read()
        
def WriteFile(path, contents):
    with open(path, 'w') as f:
        for line in contents:
            f.write(line + "\n")

if len(sys.argv) > 1:
    config.targetFolder = sys.argv[1]
    
if len(sys.argv) > 2:
    config.outputFile = sys.argv[2]

logs = list()
fileList = list()
numFile = 0

print("Looking for log files in " + config.targetFolder)

for subdir, dir, files in os.walk(config.targetFolder):
    for file in files:
        print("Reading: " + file + ".. ")
        fileList.append(str(file))
        numFile += 1
        path = os.path.join(subdir, file)
        
        content = str(ReadFile(path))
        matches = re.findall(config.regex, content)
        logs.append(matches)
        
        print("Reading: Completed.. with %d" % len(matches))
        
print("Files parsed. calculating differences..")

differences = list()

for x in range(numFile):
    for y in range(numFile):
        numLines = len(logs[x])
    
        for z in range(numLines):
            if logs[x][z] != logs[y][z]:
                diff = logs[x][z] + " -> " + logs[y][z]
                found = fileList[x] + " - " + fileList[z] + ": " + diff
                differences.append(found)
                

if len(differences) == 0:
    print("No differences found")
else:
    for d in differences:
        print(d)

    print("Writing results in the output file")
    WriteFile(config.outputFile, differences)
    print("Outputfile created:" + config.outputFile)
