# reads in 2 text files whose names are specified on the command line,
# then concatenates the contents of those files every other word, backwards.
# Finally, the product is output to a file called output.txt

import sys      # Argv[] is a member of sys, need to import sys to use command line arguments
import os

def checkline(splitLine, index):
    words = line.split()    # List with each word on a line as an element
    out.append(words[index])

infile1 = open(sys.argv[1])
infile2 = open(sys.argv[2])
outfile = open("output.txt", "w")
flines1 = infile1.readlines()   # List with each line as an element
flines2 = infile2.readlines()
print("\n\nFirst input file:")
print(flines1)
print("\n\nSecond input file:")
print(flines2)
print("\n")
out = []

if ( flines1 != [] and flines2 != [] ):
    linecount1 = len(flines1) - 1   # Amount of lines in input file 1
    linecount2 = len(flines2) - 1   # Amount of lines in input file 2
    words1 = flines1[linecount1].split()    # List with each word on a line as an element
    words2 = flines2[linecount2].split()
    index1 = len(words1) - 1
    index2 = len(words2) - 1

    while linecount1 >= 0 and linecount2 >= 0:
        if index1 >= 0 and linecount1 >= 0:
            out.append(words1[index1] + " ")
            index1 -= 1
            # Reset word index when a new line is reached
            if index1 < 0:
                linecount1 -= 1         
                words1 = flines1[linecount1].split()
                index1 = len(words1) - 1

        if index2 >= 0 and linecount2 >= 0:
            out.append(words2[index2] + " ")
            index2 -= 1
            # Reset word index when a new line is reached
            if index2 < 0:
                linecount2 -= 1
                words2 = flines2[linecount2].split()
                index2 = len(words2) - 1

    for element in out:
        outfile.write(element)
    
    outfile.write("\n\n")
    infile1.close()
    infile2.close()
    outfile.close()
    print("Output file (Also check output.txt):")
    os.system("cat output.txt")
else:
    if ( flines1 == [] ):
        print("First input file is empty.")
    if ( flines2 == [] ):
        print("Second input file is empty.")

