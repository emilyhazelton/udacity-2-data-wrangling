
nodes_count = nodes_df['id'].count() 
ways_count = ways_df['id'].count()

n_tag_types = node_tags_df['type'].value_counts()
n_tag_keys = node_tags_df['key'].value_counts()

counties = node_tags_df[node_tags_df['key'] == 'county']
cities = node_tags_df[node_tags_df['key'] == 'city']

amenities = node_tags_df[node_tags_df['key'] == 'amenity']
a = amenities['value'].value_counts()

cuisine = node_tags_df[node_tags_df['key'] == 'cuisine']
tiger_data = node_tags_df[node_tags_df['type'] == 'tiger']
 

#write to text 
with open('output.txt','w') as f:
	f.write(str(a.head(10)))

#write dataframe to csv
#df_name.to_csv('output.csv', encoding='utf-8', index=False)
