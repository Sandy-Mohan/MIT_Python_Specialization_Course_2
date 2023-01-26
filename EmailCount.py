fname = input('Enter the file name:')
if len(fname)<1:
    fname = 'mbox-short.txt'
fh=open(fname)
count =0
for line in fh:
    if line.startswith('From') and not line.startswith('From:'):
        #print(line)
        count+=1
        words = line.split()
        email = words[1]
        print(email)
print(count)