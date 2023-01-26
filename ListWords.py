fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.split()
    count = len(words)
    for word in words:
        if word not in lst:
            lst.append(word)
        #print(word, lst)
lst.sort()
print(lst)
