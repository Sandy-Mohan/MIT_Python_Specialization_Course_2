fname = input('Enter the file name:')
fh = open(fname)
content = fh.read()
print(content)
content = content.rstrip()
print()
print(content.upper())