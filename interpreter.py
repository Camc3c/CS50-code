# this program is an math interpreter

def main():
    
    # get math equation from user
    expression = input("Expression: ")
    
    # split user input into x y z variables
    x, y, z = expression.split(" ")
    
    # convert x and z types to int
    x = float(x)
    y = str(y)
    z = float(z)
    
    # if statements to decide what mathmatical action is taken
    if y == "+":
        print(x + z)
        
    elif y == "-":
        print(x - z)
        
    elif y == "*":
        print(x * z)
        
    else:
        print(x / z)    
        

main()
    