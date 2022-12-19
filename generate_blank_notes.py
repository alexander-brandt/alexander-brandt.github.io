import os
import sys

header = 0
for line in open("Website_Names_Master.tsv"):
    tokens = line.split("\t")
    if header == 0:
        header += 1
        continue
    else:
        if os.path.exists("./notes_namefiles/" + tokens[5]):
            print("WARNING -- " + tokens[5] + " already exists.")
        else:
            file = open("./notes_namefiles/" + tokens[5], "w")
            file.write(tokens[1] + " - INCOMPLETE.")
            file.close()
    print(tokens)