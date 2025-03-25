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

cricket_details = load_data()
country_list = fetch_countries(cricket_details)
display_countries = show_list(country_list)