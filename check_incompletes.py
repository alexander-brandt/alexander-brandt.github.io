import os
import sys

header = 0
remaining = 0
for line in open("Website_Names_Master.tsv"):
    tokens = line.split("\t")
    if header == 0:
        header += 1
        continue

    for file_line in open("./notes_namefiles/" + tokens[5], encoding="utf-8"):
        if "INCOMPLETE" in file_line:
            print("File incomplete - {}".format(tokens[5]))
            remaining += 1

print("{} Files Remain.".format(str(remaining)))