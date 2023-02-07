def main():
    ## make a dictionary for the menu items
    menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    ## initiate the total amount
    total_amount = 0
    ## Forever loop for catching errors
    while True:
        try:
            ## get user input
            item = input('Item: ').title()
            ## check in entered item is in the dictionary
            if item in menu:
                ## take item amount and add it to the total amount
                total_amount += menu[item]
                ## show the user the total amount
                print('Total: $', end='')
                print('{:.2f}'.format(total_amount))

        except EOFError:
            
            print()
            break
    
main()

## Credit to Dors Coding School for assistance with this program