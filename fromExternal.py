import sys

#file from Arguments
inputFile = sys.argv[1]
outputFile = sys.argv[2]

#read from input
input = open(inputFile, "r")
output = open(outputFile, 'w')

listOfDigits = input.read()
listOfDigits = [x for x in listOfDigits if ((x!= ' ') and (x !='\n'))]

#CODE GOES HERE
#CODE GOES HERE

#listOfSolutions=
#output.write("".format())
