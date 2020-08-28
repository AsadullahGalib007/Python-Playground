import xml.etree.ElementTree as ET
data = '''<stuff>
			<users>
				<user x = "2">
					<id>001</id>
					<name>Galib</name>
				</user>

				<user x = "7">
					<id>021</id>
					<name>Chuck</name>
				</user>
			</users>
		  </stuff>'''

data = ET.fromstring(data)
lst = data.findall('users/user')
print(lst)
print('User count:', len(lst))
for item in lst:
	print('Name: ', item.find('name').text)
	print('Id: ', item.find('id').text)
	print('Attribute: ', item.get("x"))