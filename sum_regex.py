import re

filename = input('Enter the filename (S - Sample/ RA - Regex Assignment :')
if(len(filename)<1):
    filename = "regex_assignment1"
elif(filename == 'S'):
    filename = "sample_regex"
else:
    filename = "regex_assignment1"

handle = open(filename)
total = 0
for line in handle:
    numbrstr = re.findall('[0-9]+', line.strip())
    for nStr in numbrstr:
        total += int(nStr)
print(total)