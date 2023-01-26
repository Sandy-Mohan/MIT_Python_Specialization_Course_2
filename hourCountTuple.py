name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
hour = dict()

# spliting time and saving it in a dict
def timeDict(file):
    for line in handle:
        if line.startswith("From") and not line.startswith("From:"):
            words = line.strip().split()
            # print(words)
            time = words[5].split(':')
            # print(time)
            hour[time[0]] = hour.get(time[0], 0) + 1
            # print(hour)
            items = hour.items()
            sortedDict = sorted(items)
            # print(sortedDict)
    return sortedDict

# sorting dictionary
def sortDict(dict):
    for k,v in dict:
        print(k,v)

sortedHour = timeDict(handle)
sortDict(sortedHour)
