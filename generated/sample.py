import os
import pprint
directory_path = '/home/ubuntuserver/SAI-Challenger/tests/generated'
for root, dirs, files in os.walk(directory_path):
    for file in files:
        print(file)
