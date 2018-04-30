import time
start = time.time()

# Code

import re
import os
import datetime
from collections import Counter

allMsgUnFormatted = []
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
				result = re.findall('<div id="(\d*?)" title="(.*?)" time="(.*?)" class="(.*?)"><span class="message-text">(.*?)<\/span>.*?</div>(?s)', fbFileContent, flags=0)
				for i in result:
					if i[4] is not '':
						allMsg.append((i[0], i[1], datetime.datetime.strptime(i[2], "%m/%d/%Y %I:%M:%S %p"), i[3], i[4]))
		break;

# time="3/16/2018 8:08:52 PM" <- Sample date

allMsgC = []

for msg in allMsg:
	allMsgC.append(msg[4].lower())

for i in range(0, 25):
	print((Counter(allMsgC).most_common(25))[i])

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

end = time.time()
print('Time to process:', '{:.5f}'.format(((end - start)*1000)) + 'ms')
