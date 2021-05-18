
import xml.etree.ElementTree as ET

tree = ET.parse('config.xml')
root = tree.getroot()
for child in root:
    if child.tag == 'url':
        print('found url')
        login = child.text
    if child.tag == 'login':
        print('found login')
        url = child.text
print(login, url)
    