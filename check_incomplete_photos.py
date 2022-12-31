import os
import sys

header = 0
remaining = 0
for line in open("Website_Names_Master.tsv"):
    tokens = line.split("\t")
    if header == 0:
        header += 1
        continue

    if not os.path.exists('pictures_namefiles/' + tokens[6]):
        print("File incomplete - {}".format(tokens[6]))
        remaining += 1

print("{} Files Remain.".format(str(remaining)))