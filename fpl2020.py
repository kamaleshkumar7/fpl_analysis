import requests
import pandas as pd
import numpy as np
import sqlite3

def generate_team(players_df):
	i = 0
	gw_team = pd.DataFrame(columns = players_df.columns)
	team = {"Burnley":3,"Wolves":3,"Sheffield Utd":3,"Leicester":3,"Liverpool":3,"Man City":3,"Southampton":3,"Brighton":3,"Newcastle":3,"Chelsea":3,"Everton":3,"Crystal Palace":3,"Man Utd":3,"West Ham":3,"Aston Villa":3,"Spurs":3,"Arsenal":3,"West Brom":3,"Fulham":3,"Leeds":3}
	position = {"Goalkeeper":2,"Defender":5,"Midfielder":5,"Forward":3}
	budget = 100
	purchase = 0
	players = []
	gk = []
	defe = []
	mid = []
	forw = []
	for ind in players_df.index:
		#if(pos_done == 0):
		#	break
		if(position[players_df['position'][ind]]>0):
			if(team[players_df['team'][ind]]>0):
				position[players_df['position'][ind]] = position[players_df['position'][ind]] - 1
				team[players_df['team'][ind]] = team[players_df['team'][ind]] - 1
				i = i + 1
				if((purchase + (players_df["now_cost"][ind]/10))<95):
					#print(str(i)+") "+str(players_df['second_name'][ind]))
					purchase = purchase + (players_df["now_cost"][ind]/10)
					#print(purchase)
					if(players_df['position'][ind]=="Goalkeeper"):
						gk.append(players_df['second_name'][ind])
					if(players_df['position'][ind]=="Defender"):
						defe.append(players_df['second_name'][ind])
					if(players_df['position'][ind]=="Midfielder"):
						mid.append(players_df['second_name'][ind])
					if(players_df['position'][ind]=="Forward"):
						forw.append(players_df['second_name'][ind])
					
	players.extend(gk)
	players.extend(defe)
	players.extend(mid)
	players.extend(forw)	
	#print(len(players))			
	#print(players)	
	#print(gw_team)

def generate_team1(players_df):
	i = 0
	gw_team = pd.DataFrame(columns = players_df.columns)
	team = {"Burnley":3,"Wolves":3,"Sheffield Utd":3,"Leicester":3,"Liverpool":3,"Man City":3,"Southampton":3,"Brighton":3,"Newcastle":3,"Chelsea":3,"Everton":3,"Crystal Palace":3,"Man Utd":3,"West Ham":3,"Aston Villa":3,"Spurs":3,"Arsenal":3,"West Brom":3,"Fulham":3,"Leeds":3}
	position = {"Goalkeeper":2,"Defender":5,"Midfielder":5,"Forward":3}
	budget = 100
	purchase = 0
	players = []
	values = []
	gk = []
	defe = []
	mid = []
	forw = []
	gkv = []
	defev = []
	midv = []
	forwv = []
	for ind in players_df.index:
		#if(pos_done == 0):
		#	break
		if(position[players_df['position'][ind]]>0):
			if(team[players_df['team'][ind]]>0):
				position[players_df['position'][ind]] = position[players_df['position'][ind]] - 1
				purchase = purchase + (players_df["now_cost"][ind]/10)
				balance = budget - purchase
				#print(balance)
				if(balance>((position["Goalkeeper"]*4)+(position["Defender"]*5)+(position["Midfielder"]*5)+(position["Forward"]*5.5))):
					team[players_df['team'][ind]] = team[players_df['team'][ind]] - 1
					i = i + 1
					#print(str(i)+") "+str(players_df['second_name'][ind]))
					#print(purchase)
					#players.append(players_df['second_name'][ind])
					if(players_df['position'][ind]=="Goalkeeper"):
						gk.append(players_df['second_name'][ind])
						gkv.append(players_df["now_cost"][ind]/10)
					if(players_df['position'][ind]=="Defender"):
						defe.append(players_df['second_name'][ind])
						defev.append(players_df["now_cost"][ind]/10)
					if(players_df['position'][ind]=="Midfielder"):
						mid.append(players_df['second_name'][ind])
						midv.append(players_df["now_cost"][ind]/10)
					if(players_df['position'][ind]=="Forward"):
						forw.append(players_df['second_name'][ind])
						forwv.append(players_df["now_cost"][ind]/10)
				else:
					purchase = purchase - (players_df["now_cost"][ind]/10)
					position[players_df['position'][ind]] = position[players_df['position'][ind]] + 1

	players.extend(gk)
	players.extend(defe)
	players.extend(mid)
	players.extend(forw)
	values.extend(gkv)
	values.extend(defev)
	values.extend(midv)
	values.extend(forwv)	
	#print(values)			
	#print(players)
	#conn = sqlite3.connect('fpl.db')
	#cursor = conn.cursor()
	#for f, b in zip(players, values):
	#	print(f,b)
	#	cursor.execute("insert into roiteam values(?,?)",(f, b)) 
	#conn.commit()
	#cursor.close()
	#conn.close()	
	#print(gw_team)

def player_minutes(players_df):
	min_list = []
	team = {"Burnley":0,"Wolves":0,"Sheffield Utd":0,"Leicester":0,"Liverpool":0,"Man City":0,"Southampton":0,"Brighton":0,"Newcastle":0,"Chelsea":0,"Everton":0,"Crystal Palace":0,"Man Utd":0,"West Ham":0,"Aston Villa":0,"Spurs":0,"Arsenal":0,"West Brom":0,"Fulham":0,"Leeds":0}
	for ind in players_df.index:
		if([players_df['minutes'][ind]][0]>360):
			team[players_df['team'][ind]] = team[players_df['team'][ind]] + 1

	sortednames=sorted(team.keys(), key=lambda x:x.lower())
	#print(team)
	for i in sortednames:
		min_list.append(team[i])
		#print(team[i])
	#print(min_list)
	val = 0
	min_list = [i for i in min_list if i != val]
	return min_list	




url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
r = requests.get(url)
json = r.json()
json.keys()

elements_df = pd.DataFrame(json['elements'])
elements_type_df = pd.DataFrame(json['element_types'])
teams_df = pd.DataFrame(json['teams'])
elements_df.head()
elements_df.columns

players_df1 = elements_df[['second_name','team','element_type','selected_by_percent','now_cost','minutes','transfers_in','value_season','total_points']]
players_df1['position'] = players_df1.element_type.map(elements_type_df.set_index('id').singular_name)
players_df1.head()
players_df1['team'] = players_df1.team.map(teams_df.set_index('id').name)
players_df1['value'] = players_df1.value_season.astype(float)
players_df1['total_points'] = players_df1.total_points
#min_list = player_minutes(players_df1)
new_df1 = players_df1.sort_values('total_points',ascending=False)
#print(new_df1)
generate_team1(new_df1)
players_df = elements_df[['second_name','team','element_type','selected_by_percent','now_cost','minutes','transfers_in','value_season','total_points']]
players_df['position'] = players_df.element_type.map(elements_type_df.set_index('id').singular_name)
players_df.head()

players_df['team'] = players_df.team.map(teams_df.set_index('id').name)
players_df['value'] = players_df.value_season.astype(float)
players_df.sort_values('value',ascending=False).head(30)
new_df = players_df.sort_values('value',ascending=False)
generate_team(new_df)
generate_team1(new_df)
pivot = players_df.pivot_table(index='position',values='value',aggfunc=np.mean).reset_index()
pivot.sort_values('value',ascending=False)

players_df = players_df.loc[players_df.value > 0]
pivot = players_df.pivot_table(index='position',values='value',aggfunc=np.mean).reset_index()
pivot.sort_values('value',ascending=False)

team_pivot = players_df.pivot_table(index='team',values='value',aggfunc=np.mean).reset_index()
team_pivot1 = team_pivot
#team_pivot1["mins"] = min_list
print(team_pivot1)
#conn = sqlite3.connect('fpl.db')
#cursor = conn.cursor()
#for ind in team_pivot1.index:
	#cursor.execute("insert into teamrot (team,value,mins)values(?,?,?)",(team_pivot1['team'][ind],team_pivot1['value'][ind],str(team_pivot1['mins'][ind]))) 
#conn.commit()
#cursor.close()
#conn.close()	
teamp = team_pivot.sort_values('value',ascending=False)
#print(teamp)
fwd_df = players_df.loc[players_df.position == 'Forward']
mid_df = players_df.loc[players_df.position == 'Midfielder']
def_df = players_df.loc[players_df.position == 'Defender']
goal_df = players_df.loc[players_df.position == 'Goalkeeper']

goal_df = goal_df.sort_values('value',ascending=False).head(10)
def_df = def_df.sort_values('value',ascending=False).head(10)
mid_df = mid_df.sort_values('value',ascending=False).head(10)
fwd_df = fwd_df.sort_values('value',ascending=False).head(10)
#print(goal_df)
#print(def_df)
#print(mid_df)
#print(fwd_df)

#conn = sqlite3.connect('fpl.db')
#cursor = conn.cursor()
#for ind in fwd_df.index:
	#cursor.execute("insert into forval values(?,?,?)",(fwd_df['second_name'][ind],fwd_df['team'][ind],str(fwd_df['now_cost'][ind]/10))) 
#conn.commit()
#cursor.close()
#conn.close()	
#players_df.to_csv('fpl_data.csv')

	