def create_character(character_name: str, strength: int, intelligence: int, charisma: int):

    # String tests
    if not isinstance(character_name, str):
        return "The character name should be a string"
    if character_name == '':
        return "The character should have a name"    
    if " " in character_name:
        return "The character name should not contain spaces"
    if len(character_name) > 10:
        return "The character name is too long"

    # Integer tests
    if not all(type(stat) is int for stat in (strength, intelligence, charisma)):
        return "All stats should be integers"
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    if charisma + strength + intelligence != 7:
        return "The character should start with 7 points"

    max_point = 10
    full_dot = '●'
    empty_dot = '○'
    no_strength = max_point - strength
    no_intelligence = max_point - intelligence 
    no_charisma = max_point - charisma


    strength_point = (strength * full_dot) + (no_strength * empty_dot)
    intelligence_point = (intelligence * full_dot) + (no_intelligence * empty_dot)
    charisma_point = (charisma * full_dot) + (no_charisma * empty_dot)
    final_result = f"{character_name}\n STR {strength_point}\n INT {intelligence_point}\n CHA {charisma_point}"
    return final_result

if __name__ == "__main__":
    print(create_character('ren', 4, 2, 1))
    print(create_character('noble', 14, 5, 1))
    print(create_character('blau', 0, 0, 7))

