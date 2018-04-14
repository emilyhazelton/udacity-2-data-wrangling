import re

### REVIEW MATCHES FOR REG EXP TO UPDATE 'MAPPING' LIST ###
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

improper_st_names = []
def review_streets(st_value):
	m = street_type_re.search(st_value)
	if m:
		street_type = m.group()
		if street_type not in expected: 
			improper_st_names.append(str(street_type))

#streets = pd.Series(node_tags_df[node_tags_df['key'] == 'street']['value'])
#streets.map(review_streets)
#print(improper_st_names)

# Street types to ignore when building improper type list
expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", "Trail", "Parkway", "Commons", "Way", "West","North","East","South","Northeast","Southwest","Northwest","Point","Circle","Heights","Rise","Gardens","Terrace","Meadows","Southeast","Loop","Alley","Highway","Broadway","Crescent","Bend","Gate","Estates","Market","Ridge","Run","Meadow","Woods","View","Center","Landing","Walk","Row","Plaza","Speedway","Division","Spur","Station","Vista","Close","Esplanade"]

### STREET TYPES TO FIX ###
mapping = {
	"St": "Street", 
	"St.": "Street", 
	"ST": "Street",
	"st": "Street",
	"Rd.": "Road", 
	"Rd": "Road",
	"Ave": "Avenue",
	"avenue": "Avenue",
	"AVENUE": "Avenue",
	"Ave.": "Avenue",
	"Dr": "Drive",
	"Ct": "Court",
	"Blvd": "Boulevard",
	"Ln.": "Lane",
	"Pl": "Place",
	"Hwy": "Highway"
	}
	  
### CLEAN STREET TYPES ###
def update_name(name, mapping=mapping):
	abbrev = street_type_re.search(name).group(0)
	if abbrev in mapping:
		name = re.sub(street_type_re, mapping[abbrev], name)
	return name

new_st_list = []
def evaluate_street(st_value):
	m = street_type_re.search(st_value)
	if m:
		street_type = m.group()
		if street_type not in expected: #fix incorrect label with mapping
			fixed_name = update_name(st_value)
			new_st_list.append(fixed_name) 
			#print(st_value, " => ", fixed_name)
		else:
			new_st_list.append(st_value)
	else:
		new_st_list.append(st_value)

value = pd.Series(node_tags_df['value'])
value.map(evaluate_street)
node_tags_df.drop('value',axis=1,inplace=True)
node_tags_df.insert(2,'value', new_st_list)


