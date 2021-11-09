# Program where you input your ingredients and it tells you what recipe you can make

recipes = {
    'omlette': ['egg','onion','mushroom'],
    'pizza' : ['flour','cheese','pepperoni'],
    'hot dog' : ['hot dog','bun','ketchup'],
    'peanut butter cookies': ['peanut butter','sugar','egg'],
    'chili-glazed salmon' : ['salmon','chili','scanllion'],
    'mac and cheese' : ['milk','macaroni','cheddar']
}

class Cookbook:

    def __init__(self, recipes):
        self.recipes = recipes
        self.food_search_list = []

    def search_recipes(self):
        # returns key of recipes if food_search_list matches, otherwise returns no match
        current_key = ''
        for key, value_list in self.recipes.items():
            current_key = key
            index_of_search_list = 0
            for food in value_list:
                if all(item in self.food_search_list for item in value_list):
                    return current_key
        return 'No match'

    def prompt(self):
        # prompts users to update the class search list
        food_search_list = []
        while True:
            food = input('Enter a food: ')
            if food == '':
                break
            food_search_list.append(food.rstrip('s'))
        self.food_search_list = food_search_list
        
    def to_string(self):
        # prints out the class dictionary to the terminal
        print(f"Recipes:")
        for key, value in self.recipes.items():
            print(f'{key.ljust(20, "-")}{value}')


def main():
    cookbook = Cookbook(recipes)
    cookbook.prompt()
    print(f'With these ingredients {cookbook.food_search_list} you are able to make: {cookbook.search_recipes()}')

main()


