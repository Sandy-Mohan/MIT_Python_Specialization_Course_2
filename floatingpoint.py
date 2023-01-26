fname = input("Enter file name: ")
count = 0
value = 0.0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    print(line.strip())
    count+=1
    pos = line.find(':')
    number = line[pos+1:]
    value+=float(number)

print(count)
print(value)
print("Average spam confidence:", (value/count))
