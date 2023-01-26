name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
sender = dict()
# to get max key
def maxSender(max):
    for key, value in sender.items():
        if value == max:
            return key

# to get max value
def maxCount(sender):
    count = list(sender.values())
    maxCount = max(count)
    return maxCount

# to iterate thru' the file and build a dictionary
def buildDict(handle):
    user = dict()
    for line in handle:
        if line.startswith('From') and not line.startswith('From:'):
            words = line.split()
            senderEmail = words[1]
            # print(senderEmail)
            user[senderEmail] = user.get(senderEmail, 0) + 1
    return user

sender = buildDict(handle)
maxNum = maxCount(sender)
maxEmail = maxSender(maxNum)
print(maxEmail, maxNum)


