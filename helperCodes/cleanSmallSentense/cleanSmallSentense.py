from os import listdir
from os.path import isfile, join

source = 'Data'
destination = 'CleanData'

minSize = 2

allFiles = listdir(source)
doneFiles = listdir(destination)
for file in allFiles:
    if file not in doneFiles:
        fullSource = join(source, file)
        fullDestination = join(destination, file)
        reader = open(fullSource)
        writer = open(fullDestination, 'w')
        for line in reader:
            spaces = line.count(' ')
            if spaces >= minSize and spaces*2 < len(line):
                writer.write(line)
        writer.close()