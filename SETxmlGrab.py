import xml.etree.ElementTree

#Load XML file 
xml = xml.etree.ElementTree.ElementTree(file='set.xml')
root = xml.getroot()

#list elements
urls = root.findall('url')

#parse param elements
for url in urls:
	for param in url.findall('param'):
		param_text = param.text
		print param_text
#		if param_text.startswith('username='):