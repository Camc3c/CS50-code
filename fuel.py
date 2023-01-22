## CS50 Fuel Gauge problem
## Program asks user for a fraction input. Program returns F E or percent based on the user input

## define main function
def main():
    ## set while loop, if program returns error, program asks for inout again
    while True:
        ## Get the fuel input from user
        fuel = input('Fraction: ')
        ## Try statement
        try:
            ## Splits user input into an X and Y value
            x, y = fuel.split('/')
            ## Initiate X and Y value as ints
            new_x = int(x)
            new_y = int(y)
            ## Devide X and Y value
            fraction = (new_x/new_y)
            ## if fraction is greater than 1 program asks for input again
            if fraction <= 1:
                break
        ## Except statement
        except (ValueError, ZeroDivisionError):
            pass
    ## Calculate percent of the fraction
    percent = int(fraction) * 100
    ## if calculated percent equals less than or equal to 1 program prints E
    if percent <= 1:
        print('E')
    ## if calculated percent is greaer than or equal to 99 program prints F
    elif percent >= 99:
        print('F')
    ## prints percent
    else:
        print(f'{percent}%')

main()