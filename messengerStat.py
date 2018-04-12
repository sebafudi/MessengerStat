import time
start = time.time()

# Code

import re
from os import listdir
import datetime
from collections import Counter

allMsgUnFormatted = []
allMsg = []
# path = ''
path = input("Location to Messenger Files: ")
path = path.replace("\"", "")
print(path)
# path = '.\\MessengerFiles'

for filename in listdir(path):	# for every file in dir
	if re.match("Counter for Messenger.*?(\d*?).html", filename):	# check for name
		with open(path + '\\' + filename, encoding='utf-8') as fbFile:	# open file
			fbFileContent = fbFile.read()	# read file
		result = re.findall('<div id="(\d*?)" title="(.*?)" time="(.*?)" class="(.*?)"><span class="message-text">(.*?)<\/span>.*?</div>(?s)', fbFileContent, flags=0)	# scan for messages regex
		for i in result:
			if i[4] is not '':
				# allMsg.append((datetime.datetime.strptime(i[2], "%m/%d/%Y %I:%M:%S %p")).month)	# create allMsg tuple
				allMsg.append((i[0], i[1], datetime.datetime.strptime(i[2], "%m/%d/%Y %I:%M:%S %p"), i[3], i[4]))	# create allMsg tuple

# print(allMsg)
# allMsg = [(msg[0], msg[1], datetime.datetime.strptime(msg[2], "%m/%d/%Y %H:%M:%S %p"), msg[3], msg[4]) for msg in allMsg]

for msg in sorted(allMsg, key=lambda x: x[2], reverse=False):
 	print(msg[0], msg[1], msg[2], msg[3], msg[4])

# /Code

end = time.time()
print('Time to process:', '{:.5f}'.format(((end - start)*1000)) + 'ms')
