## CS50 Nutrition Facts program
## Python code that ask the user for an item and returns the items calories

def main():
    ## Initiate a dictionary that holds fruits and their calorie value
    fda_calories_list = {'apple': 130,
            'avocado': 50,
            'banana': 110,
            'kiwifruit': 90,
            'lemon': 15,
            'cantaloupe': 50,
            'grapefruit': 60,
            'honeydew melon': 50,
            'lime': 20,
            'nectarine': 60,
            'orange': 80,
            'peach': 60,
            'pear': 100,
            'pineapple': 50,
            'plums': 70,
            'strawberries': 50,
            'sweet cherries': 100,
            'tangerine': 50,
            'watermelon': 80}
    
    ## Get a input from the user as a fruit
    fruit = input('Item: ')
    fruit = fruit.lower()

    ## if statement, If the fruit is not in the dictionary display nothing
    if fruit in fda_calories_list:
        fruit_calories = fda_calories_list[fruit]
        print(f'Calories: {fruit_calories}')
    else:
        print('')
        
main()