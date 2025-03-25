import yaml, random

def load_data():
    with open('./cricket.yaml', 'r') as file:
        return yaml.safe_load(file)

def fetch_countries(cricket_data):
    country_list = []
    for team in cricket_data.get('teams'):
        country_list.append(team.get('Country'))
    return country_list

def show_list(any_list):
    for idx, country in enumerate(any_list, start=1):
        print(f"{idx}. {country}")

def toss():
    return random.choice(['H', 'T'])

def fetch_players(cric_data, team, role):
    players_ls = []
    for t in cric_data.get('teams'):
        if t['Country'] == team:
            for player in t['Players']:
                if player['role'] == role:
                    players_ls.append(player['name'])
    return players_ls

def choose_teams(country_list):
    print("Welcome! Choose your team:")
    for idx, country in enumerate(country_list, start=1):
        print(f"{idx}. {country}")
    print(f"{len(country_list) + 1}. Exit")

    user_team = None
    opponent_team = None

    while not user_team:
        choice1 = input("Enter the number corresponding to your team choice: ")
        try:
            if int(choice1) == len(country_list) + 1:
                print("Exiting the program.")
                exit()
            user_team = country_list[int(choice1) - 1]
            print(f"You chose {user_team} as your team.")
        except (IndexError, ValueError):
            print("Invalid choice. Please enter a valid number.")

    while not opponent_team:
        choice2 = input("You want to play against: ")
        try:
            if int(choice2) == len(country_list) + 1:
                print("Exiting the program.")
                exit()
            opponent_team = country_list[int(choice2) - 1]
            if opponent_team == user_team:
                print("You cannot choose the same team twice. Please choose a different team.")
                opponent_team = None
            else:
                print(f"You chose {opponent_team} as the opponent team.")
        except (IndexError, ValueError):
            print("Invalid choice. Please enter a valid number.")

    return user_team, opponent_team

def perform_toss():
    print("Choose H for Heads, T for Tails, or E for Exit:")
    user_choice = input("Enter your choice: ").upper()
    if user_choice == 'E':
        print("Exiting the program.")
        exit()
    elif user_choice in ['H', 'T']:
        toss_result = toss()
        print(f"Toss result: {toss_result}")
        if user_choice == toss_result:
            print("You won the toss!")
        else:
            print("You lost the toss.")
    else:
        print("Invalid choice. Please enter H, T, or E.")
        perform_toss()

cricket_details = load_data()
country_list = fetch_countries(cricket_details)
# display_countries = show_list(country_list)
user_team, opponent_team = choose_teams(country_list)
perform_toss()
get_players_by_role_user_team = fetch_players(cricket_details, user_team, "Batsman")
get_players_by_role_opponent_team = fetch_players(cricket_details, opponent_team, "Batsman")
print(f"Players in {user_team}:")
show_list(get_players_by_role_user_team)
print(f"Players in {opponent_team}:")
show_list(get_players_by_role_opponent_team)