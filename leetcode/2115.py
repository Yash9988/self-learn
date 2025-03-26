"""
2115. Find All Possible Recipes from Given Supplies [MEDIUM]

You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients.
The i-th recipe has the name recipes[i], and you can create it if you have all the needed ingredients from
ingredients[i]. A recipe can also be an ingredient for other recipes, i.e., ingredients[i] may contain a string that is
in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, and you have an
infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.


Example 1:
Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
Output: ["bread"]

Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".


Example 2:
Input:  recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]],
        supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich"]

Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".


Example 3:
Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],
["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich","burger"]

Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".


Constraints:

    -> n == recipes.length == ingredients.length
    -> 1 <= n <= 100
    -> 1 <= ingredients[i].length, supplies.length <= 100
    -> 1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
    -> recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English letters.
    -> All the values of recipes and supplies combined are unique.
    -> Each ingredients[i] does not contain any duplicate values.


Concepts: DP, BFS, Topological Sort (Kahn's Algorithm)
"""


# Optimised Solution
def findAllRecipes(recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
    available_supplies = set(supplies)                              # Obtain the set of supplies
    in_degree = {}                                                  # Dict to track in-degrees of recipes

    # Dicts for cross-conversions
    ingredient_to_recipes = {}
    recipe_to_ingredients = {}

    for i, recipe in enumerate(recipes):                            # Iterate through the recipes
        recipe_ingredients = ingredients[i]                         # Obtain the ingredients for the curr-recipe
        recipe_to_ingredients[recipe] = recipe_ingredients          # Update the dict with recipe ingredients
        in_degree[recipe] = len(recipe_ingredients)                 # Update the recipe in-degree

        for ingredient in recipe_ingredients:                       # Iterate through the ingredients
            if ingredient not in ingredient_to_recipes:             # Check if ingredient present in the dict
                ingredient_to_recipes[ingredient] = []              # Initialise the ingredient as a key

            ingredient_to_recipes[ingredient].append(recipe)        # Add the recipe under the ingredient

    queue = list(available_supplies)                                # List to process the supplies
    result = []                                                     # List to store the result

    while queue:                                                    # While the queue is non-empty
        current = queue.pop(0)                                      # Pop the first element of the queue

        if current in recipe_to_ingredients:                        # Check if curr-ele is a recipe
            result.append(current)                                  # Append the element to the list

        if current in ingredient_to_recipes:                        # Check if curr-ele is an ingredient
            # Iterate through all the possible recipes for the curr-ingredient
            for dependent_recipe in ingredient_to_recipes[current]:
                in_degree[dependent_recipe] -= 1                    # Decrement the in-degree for the recipe

                if in_degree[dependent_recipe] == 0:                # Check if the in-degree for the recipe is zero
                    queue.append(dependent_recipe)                  # Append the recipe to the queue

    return result                                                   # Return the result
