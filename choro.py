import pandas, folium, json

data = pandas.read_csv('mammoth_data.csv')
quantities = data['abd']
quantities = quantities.fillna(value=1)

data['quantity']=quantities

state_data_groups = data.groupby(by=['state']).sum().reset_index()

states_abbr = json.load(open('us_states_abbr.json'))

state_list = list(states_abbr.keys())

all_state_zeroes = pandas.DataFrame({'state': state_list, 'quantity': 0})

all_state_data = state_data_groups.append(all_state_zeroes)
all_state_data = all_state_data.drop_duplicates('state', keep='first')
state_data_groups = all_state_data.replace(states_abbr)

us_states_file = 'us_state_abbr.json'

print(state_data_groups)

