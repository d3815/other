import re
import sys


allitems = []
event = sys.argv[1]


with open ('items.json', 'r') as rfile: 
	for line in rfile:
		pattern = re.compile(r'^\t"(?!col).*' + event + r'.*"')
		match = re.findall(pattern, line)
		if match:
			allitems.append(match[0])

list_uniq_item = list(set(allitems))
list_uniq_item.sort()

with open('output.txt', 'w', encoding='utf-8') as wfile:
	for i in list_uniq_item:
		wfile.write(i + '\n')


print('\n'.join(list_uniq_item))
print(len(list_uniq_item))
input()
