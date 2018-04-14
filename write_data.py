### Write TO CSV ###
def create_csv(dataframe,output_name):
	dataframe.to_csv(output_name, encoding='utf-8', index=False)

'''create_csv(nodes_df, 'csv_output/nodes.csv')
create_csv(node_tags_df, 'csv_output/nodes_tags.csv')
create_csv(ways_df, 'csv_output/ways.csv')
create_csv(way_nodes_df, 'csv_output/ways_nodes.csv')
create_csv(way_tags_df,'csv_output/ways_tags.csv')'''

### WRITE TO SQL ###
db_loc = "C:\Users\erhaz\projects\udacity\open-street-maps\OSM.db"
conn = sqlite3.connect(db_loc)

nodes_types = {"id": "INTEGER PRIMARY KEY NOT NULL", "lat": "REAL", "lon": "REAL","user": "TEXT","uid":"INTEGER","version":"INTEGER","changeset":"INTEGER","timestamp":"TEXT"}
nodes_df.to_sql('nodes',conn,if_exists='replace',index=False,dtype=nodes_types)

nodes_tags_types = {"id":"INTEGER REFERENCES nodes(id)","key": "TEXT","value":"TEXT","type":"TEXT"}
node_tags_df.to_sql('nodes_tags',conn,if_exists='replace',index=False,dtype=nodes_tags_types)

ways_tags_types = {"id": "INTEGER PRIMARY KEY NOT NULL", "user": "TEXT","uid":"INTEGER","version":"TEXT","changeset":"INTEGER","timestamp":"TEXT"}
ways_df.to_sql('ways',conn,if_exists='replace',index=False,dtype=ways_tags_types)

ways_tags_types = {"id":"INTEGER REFERENCES ways(id)","key": "TEXT","value":"TEXT","type":"TEXT"}
node_tags_df.to_sql('nodes_tags',conn,if_exists='replace',index=False,dtype=ways_tags_types)

ways_nodes_types = {"id": "INTEGER NOT NULL REFERENCES ways(id)", "node_id": "INTEGER NOT NULL REFERENCES nodes(id)","position": "INTEGER NOT NULL"}
way_tags_df.to_sql('ways_nodes',conn,if_exists='replace',index=False,dtype=ways_nodes_types)

conn.close()