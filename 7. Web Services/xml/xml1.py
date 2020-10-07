import xml.etree.ElementTree as ET 
data = '''<person>
			<name>Galib</name>
			<phone type = "intl">
				+8801521426851
			</phone>
			<email hide = "yes"/>
		  </person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))