# CodeQuest: The Python Adventure
# main.py

# Global variables for player stats
player_level = 1
player_xp = 0
player_skill_points = 0

# Global variables for player stats
player_info = {
    'name': '',
    'class': '',
    'level': 1,
    'xp': 0,
    'skill_points': 0,
    'inventory': {
        'gold': 100,
        'items': ['Map', 'Health Potion', 'Scroll of Wisdom']
    }
}

# Quests and NPC interactions
questline = {
    '1': {
        'title': 'The Village of Variables',
        'description': 'Help the villagers with basic variable management tasks.',
        'xp_reward': 50,
        'completed': False
    },
    '2': {
        'title': 'The Looping Forest',
        'description': 'Navigate through the forest using loops to find a hidden treasure.',
        'xp_reward': 100,
        'completed': False
    },
    '3': {
        'title': 'The Function Fortress',
        'description': 'Solve challenges in the fortress by using functions effectively.',
        'xp_reward': 150,
        'completed': False
    }
}

npcs = {
    'wise_sage': {
        'name': 'Wise Sage',
        'dialogue': "Welcome, young adventurer! Seek wisdom and guidance on your journey.",
        'quests': {
            '1': "Ah, I see you've helped the villagers with variables. Continue your journey to unlock more secrets.",
            '2': "The Looping Forest holds many mysteries. Only those who master loops can uncover its secrets.",
            '3': "You've reached the Function Fortress! Prepare yourself for the challenges that lie ahead."
        }
    },
    'blacksmith': {
        'name': 'Blacksmith',
        'dialogue': "Greetings! I can craft powerful tools to aid you in your quest for a price."
    }
}

def main():
    # Display game title and introduction
    print("Welcome to CodeQuest: The Python Adventure!")
    print("Embark on an epic journey to master Python programming while exploring a fantastical world filled with challenges and adventures.")
    print("Are you ready to begin your quest?\n")

    # Prompt the player to start the game or exit
    start_game = input("Type 'start' to begin your adventure, or 'exit' to quit: ")

    if start_game.lower() == 'start':
        start_adventure()
    elif start_game.lower() == 'exit':
        print("Thank you for considering CodeQuest: The Python Adventure. Goodbye!")
    else:
        print("Invalid input. Please type 'start' to begin the adventure or 'exit' to quit.")

def start_adventure():
    # Welcome message
    print("\nWelcome to the world of CodeQuest!")
    print("You find yourself in the Village of Variables, where your coding journey begins.")

    # Player customization
    player_info['name'] = input("What is your name, adventurer? ")
    player_info['class'] = input("Choose your class (e.g., Coder, Hacker, Programmer): ")

    # Game loop
    while True:
        print("\nYou have several options:")
        print("1. Explore the village")
        print("2. Start a coding challenge")
        print("3. Check your inventory")
        print("4. Visit the wise sage")
        print("5. Exit the village")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            explore_village()
        elif choice == '2':
            start_coding_challenge()
        elif choice == '3':
            check_inventory()
        elif choice == '4':
            visit_wise_sage()
        elif choice == '5':
            print("You leave the Village of Variables. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

def explore_village():
    print("\nYou explore the Village of Variables and interact with the villagers.")

    while True:
        print("\nYou encounter a villager who needs your help:")
        print("1. Help the villager with variables")
        print("2. Continue exploring")
        print("3. Return to the village entrance")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            help_villager_with_variables()
        elif choice == '2':
            continue_exploring()
        elif choice == '3':
            print("You return to the village entrance.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 3.")

def help_villager_with_variables():
    print("\nThe villager needs assistance with managing variables.")
    # Implement quest logic related to variables
    complete_quest('1')  # Complete the quest related to variables

def complete_quest(quest_id):
    if not questline[quest_id]['completed']:
        print("\nYou complete the quest and gain experience!")
        player_info['xp'] += questline[quest_id]['xp_reward']
        questline[quest_id]['completed'] = True
        check_level_up()

def check_level_up():
    # Check if player has enough XP to level up
    if player_info['xp'] >= 100 * player_info['level']:
        print("Congratulations! You've leveled up!")
        player_info['level'] += 1
        player_info['skill_points'] += 1

def continue_exploring():
    print("\nYou continue exploring the village.")
    # Implement additional exploration content

def start_coding_challenge():
    print("\nYou decide to take on a coding challenge.")

    while True:
        print("\nChoose a coding challenge:")
        print("1. The Looping Forest")
        print("2. The Function Fortress")
        print("3. Return to the village")

        challenge_choice = input("Enter your choice (1-3): ")

        if challenge_choice == '1':
            looping_forest_challenge()
        elif challenge_choice == '2':
            function_fortress_challenge()
        elif challenge_choice == '3':
            print("You return to the village.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 3.")

def looping_forest_challenge():
    print("\nYou enter the Looping Forest and face a challenge involving loops.")
    # Implement coding challenge related to loops

def function_fortress_challenge():
    print("\nYou approach the Function Fortress and encounter a challenge that requires functions.")
    # Implement coding challenge related to functions

def check_inventory():
    print("\nYou check your inventory.")

    print("Current inventory:")
    print("Gold:", player_info['inventory']['gold'])
    print("Items:", player_info['inventory']['items'])

    # Player progression
    print("\nPlayer Level:", player_info['level'])
    print("Experience Points:", player_info['xp'])
    print("Skill Points:", player_info['skill_points'])

def visit_wise_sage():
    print("\nYou visit the wise sage for guidance.")
    sage_dialogue = npcs['wise_sage']['dialogue']
    print(sage_dialogue)

    # Display available quests from the wise sage
    available_quests = []
    for quest_id, quest_info in questline.items():
        if not quest_info['completed']:
            available_quests.append((quest_id, quest_info['title']))
    if available_quests:
        print("\nAvailable Quests:")
        for quest_id, quest_title in available_quests:
            print(f"{quest_id}. {quest_title}")
        print("Choose a quest to learn more.")
        quest_choice = input("Enter quest ID (or type 'back' to return): ")
        if quest_choice == 'back':
            return
        elif quest_choice in questline:
            print(questline[quest_choice]['description'])
            print(npcs['wise_sage']['quests'][quest_choice])
        else:
            print("Invalid quest ID.")
    else:
        print("You have completed all available quests. Come back later for more challenges.")

if __name__ == "__main__":
    main()
