# Program where you input your ingredients and it tells you what recipe you can make

recipes = {
    'omlette': ['egg','onion','mushroom'],
    'pizza' : ['flour','cheese','pepperoni'],
    'hot dog' : ['hot dog','bun','ketchup']
}


def search(search_item_list, dictionary):
    current_key = ''
    for key, value_list in dictionary.items():
        current_key = key
        index_of_search_list = 0
        for food in value_list:
            if all(item in search_item_list for item in value_list):
                return current_key
    return 'No match'
        
# User input to search for recipe

selection = []
print("Please enter 3 food items to search for a recipe you can make")
while len(selection) < 3:
    choice = input("> ")
    selection.append(choice)

recipe_match = search(selection, recipes)
print(f"You are able to make a {recipe_match}")
