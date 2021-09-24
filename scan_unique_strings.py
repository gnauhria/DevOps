import os
import sys
from collections import Counter

dir_name=str(sys.argv[1])

#Check if Directory exists
if str(os.path.exists(dir_name))=='False':
    print("Directory Path not found")
    exit()


file_names=[]

#Get list of all files from all directories and subdirectories
for subdir, dirs, files in os.walk(dir_name):
    for file in files:
        file_path=os.path.join(subdir, file)
        file_names.append(file_path)

unique = []
#Create a list of all unique strings
for file in file_names:
    text_file = open(file, 'r')
    text = text_file.read()
    text = text.lower()
    words = text.split()
    for word in words:
        unique.append(word)

#Print the most common strings first along with number of occurences
for word, count in Counter(unique).most_common():
    print "{} {}".format(word, count)
