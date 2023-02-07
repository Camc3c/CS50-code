## CS50 grcery problem
## A program that takes input of the users grocery list and outputs
## all the items in alphabetical order with the number of each item

## Def main
def main():
    ## Create empty dictionary
    grocery = {}
    ## Forever loop
    while True:
        try:
            ## Get user input
            item = input().lower()
            ## Check if the item is already in the dictionary
            if item in grocery:
                ## If it is add one in the count
                grocery[item] += 1
            ## Else add the item into the dictionary
            else :
                grocery[item] = 1
        except EOFError:
            ## print all items in alphabetical order
            for key in sorted(grocery.keys()):
                print(grocery[key], key.upper())
            ## stop the while loop
            break

main()

## Credit to Dors Coding School for assistance with this program