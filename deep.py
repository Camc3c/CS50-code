# Program that asks the user for a the answer Great Question of Life

def main():
    
    # gets user input
    the_question = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
    
    # converts input to lower case to allow case-insensitively input
    the_question = the_question.lower()
    
    # if statement that decides if the answer is correct
    if the_question == "42":
        print("Yes")
    elif the_question == "forty-two":
        print("Yes")
    elif the_question == "forty two":
        print("Yes")
    else:
        print("No")
        
main()
    
    