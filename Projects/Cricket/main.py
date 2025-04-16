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
    players_with_role = []
    print(role)
    for t in cric_data.get('teams'):
        if t['Country'] == team:
            for player in t['Players']:
                if player['role'] == role:
                    players_with_role.append(player['name'])
    return players_with_role

def choose_team(any_list):
    any_map = {}
    sl_no = 1
    for a in any_list:
        any_map[sl_no] = a
        sl_no += 1
    for k, v in any_map.items():
        print(f"{k} - {v}")
    choice = int(input("Enter the number corresponding to your choice: "))
    for x, y in any_map.items():
        if choice == x:
            print(f"You Chose {y} as your team")

def perform_toss():
    toss_result = toss()
    print("Choose H for Heads, T for Tails, E for exit")
    user_call = input().upper()
    if user_call == "E":
        print("Exiting the program, have a good day")
        exit()
    elif user_call in ["H", "T"]:
        print(f"Toss result: {toss_result}")
        if user_call == toss_result:
            print("You have won the toss")
        else:
            print("You have lost the toss")
    else:
        print("You have entered the wrong choice")

cricket_details = load_data()
country_list = fetch_countries(cricket_details)


print("------WELCOME TO CRICKET------")
print("Choose your team")
choose_team(country_list)
perform_toss()