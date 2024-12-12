
import random
import time

def create_character():
    # Get character attributes from the user with validation for specific ranges
    name = input("Enter character name: ").strip()

    # Ensure attack is between 100 and 200
    attack = int(input("Enter character attack (integer between 100 and 200): "))
    while not (100 <= attack <= 200):
        print("Invalid attack value. Please enter a value between 100 and 200.")
        attack = int(input("Enter character attack (integer between 100 and 200): "))
    
    # Ensure defense is between 50 and 75
    defense = int(input("Enter character defense (integer between 50 and 75): "))
    while not (50 <= defense <= 75):
        print("Invalid defense value. Please enter a value between 50 and 75.")
        defense = int(input("Enter character defense (integer between 50 and 75): "))
    
    # Ensure health is between 150 and 175
    health = int(input("Enter character health (integer between 150 and 175): "))
    while not (150 <= health <= 175):
        print("Invalid health value. Please enter a value between 150 and 175.")
        health = int(input("Enter character health (integer between 150 and 175): "))
    
    # Special ability selection
    print("\nSelect a special ability:")
    print("1. Power Punch (Double damage for one turn)")
    print("2. Helping Hand (Heals 30% of current health for one turn)")
    print("3. Defensive Shield (Doubles defense for one turn)")
    
    special_ability = input("Enter the number of the special ability you want: ").strip()
    
    # Validate special ability input
    while special_ability not in ['1', '2', '3']:
        print("Invalid choice. Please select 1, 2, or 3.")
        special_ability = input("Enter the number of the special ability you want: ").strip()

    character = {
        "name": name,
        "attack": attack,
        "health": health,
        "defense": defense,
        "special_ability": special_ability,  # Store the chosen special ability
        "special_ability_used": False
    }
    
    return character

def display_characters(characters):
    """Prints the attributes of each character in a readable format."""
    for character in characters:
        print(f"\nCharacter Name: {character['name']}")
        print(f"  Attack: {character['attack']}")
        print(f"  Health: {character['health']}")
        print(f"  Defense: {character['defense']}")
        print(f"  Special Ability: {character['special_ability']}")
        print("")

def use_special_ability(character, turn):
    """Ask if the player wants to use their special ability and apply the effect if so."""
    if character['special_ability_used']:
        return None  # Ability has already been used
    
    use_ability = input(f"\n{character['name']}, do you want to use your special ability this turn? (y/n): ").strip().lower()
    
    if use_ability == 'y':
        if character['special_ability'] == '1':
            print(f"{character['name']} uses Power Punch! Their attack is doubled for this turn!")
            return "Power Punch"
        elif character['special_ability'] == '2':
            heal_amount = character['health'] * 0.30
            character['health'] += heal_amount
            print(f"{character['name']} uses Helping Hand! They heal {heal_amount:.2f} health!")
            return "Helping Hand"
        elif character['special_ability'] == '3':
            print(f"{character['name']} uses Defensive Shield! Their defense is doubled for this turn!")
            return "Defensive Shield"
    return None

def battle(character1, character2):
    print(f"Battle Start: {character1['name']} vs {character2['name']}!\n")
    
    # Clone health values to modify without affecting the original character data
    character1_health = character1['health']
    character2_health = character2['health']
    
    turn = 1  # Track which turn it is
    while character1_health > 0 and character2_health > 0:
        print(f"--- Turn {turn} ---")
        
        # Handle Special Abilities
        ability_used1 = use_special_ability(character1, turn)
        ability_used2 = use_special_ability(character2, turn)

        # Character 1 attacks Character 2
        damage1 = random.randint(0, character1['attack']) - character2['defense']
        if ability_used1 == "Power Punch":
            damage1 *= 2  # Double the damage for Power Punch
        damage1 = max(0, damage1)  # Ensure no negative damage
        character2_health -= damage1
        print(f"{character1['name']} attacks for {damage1} damage!")
        
        if character2_health <= 0:
            print(f"\n{character2['name']} has been defeated!")
            return character1  # Character 1 wins
        
        # Add a small delay after the attack
        time.sleep(1)

        # Character 2 attacks Character 1
        damage2 = random.randint(0, character2['attack']) - character1['defense']
        if ability_used2 == "Power Punch":
            damage2 *= 2  # Double the damage for Power Punch
        damage2 = max(0, damage2)  # Ensure no negative damage
        character1_health -= damage2
        print(f"{character2['name']} attacks for {damage2} damage!")
        
        if character1_health <= 0:
            print(f"\n{character1['name']} has been defeated!")
            return character2  # Character 2 wins
        
        # Add a small delay after the attack
        time.sleep(1)

        # Display remaining health after each turn
        print(f"\n{character1['name']}'s health: {character1_health}")
        print(f"{character2['name']}'s health: {character2_health}\n")

        # Mark that special abilities have been used
        if ability_used1:
            character1['special_ability_used'] = True
        if ability_used2:
            character2['special_ability_used'] = True

        # Add a delay between turns
        time.sleep(2)

        turn += 1  # Move to the next turn

# Example usage
if __name__ == "__main__":
    # Create characters
    char1 = create_character()
    char2 = create_character()

    # Display characters' attributes before battle
    display_characters([char1, char2])

    # Start the battle
    winner = battle(char1, char2)
    print(f"\n🏆 {winner['name']} is the winner! 🏆")
