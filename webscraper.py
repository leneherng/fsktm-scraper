from bs4 import BeautifulSoup
import requests
import json
from csv import DictWriter

compArr = []

for x in range(1, 457, 1):
	url = 'http://careerportal.fsktm.um.edu.my/companylist/'
	url += str(x)

	response = requests.get(url, timeout = 15)
	content = BeautifulSoup(response.content, "html.parser")
	compObject = {}

	for comp in content.findAll('tr'):
		h = comp.find('th').text
		d = comp.find('td').text.strip().replace(' ','').replace('\n','')
		compObject[h] = d
		
	if 'Phone:' in compObject and compObject['Phone:'] == '+993331234567':
		compObject['Phone:'] = ''
			
	for comp in content.findAll('dd'):
		compObject["Add. Info:"] = comp.get_text().strip()
	
	compArr.append(compObject)

#with open('careerportal.json', 'w') as outfile:
#	json.dump(compArr, outfile)

with open('careerportal.csv', 'w') as outfile:
	writer = DictWriter(outfile, ('Name:', 'Address:','Email:','Phone:','Website:','Add. Info:'))
	writer.writeheader()
	writer.writerows(compArr)