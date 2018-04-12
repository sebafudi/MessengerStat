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

# print(allMsg)
# allMsg = [(msg[0], msg[1], datetime.datetime.strptime(msg[2], "%m/%d/%Y %H:%M:%S %p"), msg[3], msg[4]) for msg in allMsg]

for msg in sorted(allMsg, key=lambda x: x[2], reverse=False):
 	print(msg[0], msg[1], msg[2], msg[3], msg[4])

# /Code

end = time.time()
print('Time to process:', '{:.5f}'.format(((end - start)*1000)) + 'ms')
