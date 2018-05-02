import time
start = time.time()
print()

# Code

import re
import os
import datetime
from collections import Counter

allMsg = []

while True:
	path = input("Location to Messenger Files: ")
	path = path.replace("\"", "")
	if path == '':
		path = '.\\MessengerFiles'
	if os.path.isdir(path):
		for filename in os.listdir(path):
			if re.match("Counter for Messenger.*?(\d*?).html", filename):
				with open(path + '\\' + filename, encoding='utf-8') as fbFile:
					fbFileContent = fbFile.read()
				result = re.findall('<div id="(\d*?)" title="(.*?)" time="(.*?)" class="(.*?)"><span class="message-text">(.*?)<\/span>.*?<\/div>(?s)', fbFileContent, flags=0)
				for i in result:
					if i[4] is not '':
						#allMsg.append((i[0], i[1], datetime.datetime.strptime(i[2], "%m/%d/%Y %I:%M:%S %p"), i[3], i[4]))
						a = re.findall('^(.*?)\/(.*?)\/(.*?) (.*?):(.*?):(.*?) (.*?)$(?s)', i[2])[0]
						dat = datetime.datetime(int(a[2]), int(a[0]), int(a[1]), int(a[3]) if a[6] == 'AM' else (int(a[3])+12 if a[3] != '12' else 0), int(a[4]), int(a[5]))
						allMsg.append((i[0], i[1] if i[1] !='&lt;Unknown&gt;' else '*Removed*', dat, i[3], i[4]))
		break

# time="3/16/2018 8:08:52 PM" <- Sample date
# <div id="1480024555474" title="Szymon Kwaśniak" time="11/24/2016 10:55:55 PM" class="box_l"><span class="message-text">XD</span> </div> <- Sample message

allUsers = []
for msg in allMsg:
	if msg[1] not in [i[0] for i in allUsers]:
		allUsers.append([msg[1], 0])
for u in allUsers:
	j2 = [i for i in allMsg if i[1] == u[0]]
	u[1] = len(j2)
c = 1
for u in sorted(allUsers, key=lambda x: x[1], reverse=True):
	print(str(c) + '.', u[0], u[1])
	c+=1
# for user in allUsers:
# 	j2 = [i for i in allMsg if i[1] == user]
# 	print(user, len(j2))



# print(allUsers)
# j2 = [i for i in allMsg if i[1] == "&lt;Unknown&gt;"]
# for msg in j2:
# 	print(msg[1], msg[4])


# allMsgC = []
#
# for msg in allMsg:
# 	allMsgC.append(msg[4].lower())
# for i in range(0, 100):
# 	print((Counter(allMsgC).most_common(100))[i])

# print(allMsg)
# allMsg = [(msg[0], msg[1], datetime.datetime.strptime(msg[2], "%m/%d/%Y %H:%M:%S %p"), msg[3], msg[4]) for msg in allMsg]
# with open('messages1.txt', 'w', encoding='utf-8') as messagesf:
# 	for msg in sorted(allMsg, key=lambda x: x[0], reverse=False):
# 		#print(msg[0], msg[1], msg[2], msg[3], msg[4])
# 		messagesf.write(str(msg[0] + ' ' + msg[1] + ' ' + str(msg[2].date()) + ' ' + str(msg[2].time()) + ' ' +  msg[4]) + '\n')


# with open('words.txt', 'w', encoding='utf-8') as wordsf:
# 	for i in range (0, 100):
# 		wordsf.write(str(allWordsC.most_common(100)[i][0]) + ',' + str(allWordsC.most_common(100)[i][1]) + '\n')

# /Code

print()
end = time.time()
print('Time to process:', '{:.5f}'.format(((end - start)*1000)) + 'ms')
