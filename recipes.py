# Program where you input your ingredients and it tells you what recipe you can make

recipes = {
    'omlette': ['egg','onion','mushroom'],
    'pizza' : ['flour','cheese','pepperoni'],
    'hot dog' : ['hot dog','bun','ketchup']
}


def search(search_item_list, dictionary):
    current_key = ''
    number_of_matches = 0
    for key, value in dictionary.items():
        current_key = key
        index_of_search_list = 0
        for food in value:
            if food == search_item_list[index_of_search_list]:
                number_of_matches += 1
                index_of_search_list += 1
                if number_of_matches == 3:
                    return current_key
        
# User input to search for recipe

selection = []
print("Please enter 3 food items to search for a recipe you can make")
while len(selection) < 3:
    choice = input("> ")
    selection.append(choice)

recipe_match = search(selection, recipes)
print(f"You are able to make a {recipe_match}")
