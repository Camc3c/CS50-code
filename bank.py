# bank program that gives you moeny for non hello greetings

def main():
    
    # gets uses greeting
    greeting = input("Greeting: ")
    
    # removes white space in users input
    greeting = greeting.strip()
    
    # converts users input to lower case to allow case-insensitively
    greeting = greeting.lower()
    
    # if statement to decide if users input receives money
    if "hello" in greeting:
        
        print("$0")
    # checks if string starts with the letter h    
    elif greeting.startswith("h"):
        
        print("$20")
    
    else:
        
        print("$100")
        
main()