import yaml, random

def load_data():
    with open('D:\\Coding\\Learn-python\Projects\\Cricket\\cricket.yaml', 'r') as file:
        return (yaml.safe_load(file))

def fetch_countries(cricket_data):
    country_list = []
    for team in cricket_data.get('teams'):
        country_list.append(team.get('Country'))
    return country_list

def show_list(any_list):
    any_map = {}
    sl_no = 1
    for a in any_list:
        any_map[sl_no] = a
        sl_no += 1
    for k, v in any_map.items():
        print(f"{k} - {v}")
    
def toss():
    return (random.choice(['H', 'T'])) 

def fetch_players(cric_data, team, role):
    players_ls = []
    print(role, end=" ")
    for t in cric_data.get('teams'):
        if t['Country'] == team:
            for player in t['Players']:
                if player['role'] == role:
                    players_ls.append(player['name'])
    return players_ls

cricket_details = load_data()
country_list = fetch_countries(cricket_details)
display_countries = show_list(country_list)
get_players_by_role = fetch_players(cricket_details, "India", "Batsmna")