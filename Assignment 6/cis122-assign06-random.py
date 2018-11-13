'''
CIS 122 Fall 2018 Assignment 6
Author: Jacob Rammer
Partner: None
Description: Read a number txt file and display results
'''

fin = open("random_numbers.txt")

line_count = comments = line_number = total = 0
for line in fin:  # Counts line in the file
    if line[0:1] == "#":  # Counts comment lines
        comments += 1
    elif line[0:1].isdigit():  # Counts lines that are integers
        line_count += 1
        total += int(line)  # Calculates the total of all integers in file

print("Count:", line_count)
print("Comments:", comments)
print("Total:", total)
print("Average:", total / line_count)
