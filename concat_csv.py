import os

listfiles = []
path = os.getcwd()
with os.scandir(path) as listOfEntries:
    for entry in listOfEntries:
        if entry.is_file():
            if entry.name[-3:] == "csv":
                listfiles.append(entry.name)
my_file = open("Itog.txt", "a+")
for a in listfiles:
    with open(a, 'r') as f2:
        my_file.write(f2.read())

my_file.close()
