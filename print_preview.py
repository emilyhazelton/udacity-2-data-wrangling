import xml.etree.cElementTree as ET

SAMPLE_FILE = 'sample.osm'

counter = 0
for event, elem in ET.iterparse(SAMPLE_FILE):
	if counter > 250:
		break
	counter += 1

	print(elem.tag, elem.attrib)

	for child in elem:
		print('CHILD', elem.tag, elem.attrib)

	elem.clear()