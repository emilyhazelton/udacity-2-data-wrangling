import xml.etree.cElementTree as ET
import pandas as pd
import collections

OSM_FILE = 'seattle_washington.osm'
SAMPLE_FILE = 'sample.osm'

#create lists to hold different tags
nodes = []
node_tags = []
ways = []
way_tags = []
way_nds = []

for event, elem in ET.iterparse(OSM_FILE):
	#print(elem.tag,elem.attrib)
	if elem.tag == 'node':
		nodes.append(elem.attrib)
	
	elif elem.tag == 'way':
		ways.append(elem.attrib)
	
	else:
		continue

	counter = 0
	for child in elem:
		t = child.tag
		if t == 'tag':
			d = collections.defaultdict(list)
			d["id"] = elem.get("id")
			d["value"] = child.get("v")

			k = child.get("k")
			if k and ':' in k:
				l = k.split(':')
				d["type"] = l.pop(0)
				d["key"] = l[0]
			elif k:
				d["type"] = 'regular'
				d["key"] = k
			if elem.tag == 'node':
				node_tags.append(d)
			elif elem.tag == 'way':
				way_tags.append(d)	
		
		elif t == 'nd':
			d = collections.defaultdict(list)
			d["id"] = elem.get("id")
			d["node_id"] = child.get("ref")
			d["position"] = counter
			counter +=1
			way_nds.append(d)

	elem.clear()

#create data frames from lists, with columns in same order as sql schema
nodes_columns = ['id','lat','lon','user','uid','version','changeset','timestamp']
nodes_df = pd.DataFrame(nodes,columns=nodes_columns)

node_tag_columns=['id','key','value','type']
node_tags_df = pd.DataFrame(node_tags, columns=node_tag_columns)

ways_columns = ['id','user','uid','version','changeset','timestamp']
ways_df = pd.DataFrame(ways, columns=ways_columns)

way_tags_columns = ['id','key','value','type']
way_tags_df = pd.DataFrame(way_tags,columns=way_tags_columns)

way_nodes_columns = ['id','node_id','position']
way_nodes_df = pd.DataFrame(way_nds,columns=way_nodes_columns)

