
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

print(recipes)