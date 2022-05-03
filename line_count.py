import os
import sys
import io

blacklist = []

def count_lines(path, ext):
    lineCount = 0
    for entry in blacklist:
        if path.endswith(entry):
            return lineCount
        
    if os.path.isfile(path) and path.endswith(ext):
        with open(path, 'rb') as f:
            print(path)
            lines = f.readlines()
            lineCount = len(lines)
    elif os.path.isdir(path):
        with os.scandir(path) as entries:
            for entry in entries:
                lineCount += count_lines(os.path.join(path, entry.name), ext)

    return lineCount

if len(sys.argv) < 3:
    print("Path and file extension must be provided as arguments")
else:
    path = sys.argv[1]
    ext = sys.argv[2]
    for i in range(3, len(sys.argv)):
        blacklist.append(sys.argv[i])

    for entry in blacklist:
        print(entry)
    print(count_lines(path, ext))
