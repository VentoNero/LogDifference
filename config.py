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

targetFolder = "./logs"
outputFile = "./output.txt"

regex = '.*\[!>(.*)<!\].*'