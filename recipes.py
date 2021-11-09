# Program where you input your ingredients and it tells you what recipe you can make

# Importing the recipes from recipes.txt file
import csv

recipes = {}
with open('recipes.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for line in csv_reader:
        dish = line[0]
        ingredients = []
        for ingredient in line[1:]:
            ingredients.append(ingredient)
        recipes[dish] = ingredients


class Cookbook:

    def __init__(self, recipes):
        self.recipes = recipes
        self.food_search_list = []
        self.dish_match = []

    def search_recipes(self):
        # updates dish_match variable with list of matches
        matches = []
        for key, value_list in self.recipes.items():
            if all(item in self.food_search_list for item in value_list):
                matches.append(key)
        if bool(matches):
            self.dish_match = matches

    def prompt(self):
        # prompts users to update the class search list
        food_search_list = []
        while True:
            food = input('Enter a food (or blank to end): ')
            if food == '':
                break
            food_search_list.append(food.rstrip('s'))
        self.food_search_list = food_search_list

    def to_string_matches(self):
        print('\nIngredients Available:')
        for item in self.food_search_list:
            print('-' + item)
        print('\nDishes possible: ')
        for item in self.dish_match:
            print('-' + item)
        
    def to_string(self):
        # prints out the class dictionary to the terminal
        print(f"Recipes:")
        for key, value in self.recipes.items():
            print(f'{key.ljust(20, "-")}{value}')


def main():
    cookbook = Cookbook(recipes)
    cookbook.prompt()
    cookbook.search_recipes()
    cookbook.to_string_matches()

main()


