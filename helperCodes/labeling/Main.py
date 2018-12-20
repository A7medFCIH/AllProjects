from os import listdir
from os.path import isfile, join

source = 'Data'
destination = 'labelData'

labels = ['content', 'question']

allFiles = listdir(source)
doneFiles = listdir(destination)
for file in allFiles:
    if file not in doneFiles:
        fullSource = join(source, file)
        fullDestination = join(destination, file)
        reader = open(fullSource)
        writer = open(fullDestination, 'w')
        fst = True
        for label in labels:
            if not fst:
                writer.write(', ')
            writer.write(label)
            fst = False
        writer.write('\n')
        i = 1
        for line in reader:
            line = line[:-1]
            print(line)
            respnses = input(str(i) + ' respnses: ')
            i = i + 1
            writer.write(line)
            for respnse in respnses:
                writer.write(', ')
                writer.write(respnse)
            writer.write('\n')
        writer.close()