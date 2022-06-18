# A program that outputs a media type based on the users input

def main():
    
    media = input("File name: ")
    
    media = media.casefold()
    
    if media.endswith(".gif"):
        print("image/gif")
        
    elif media.endswith(".jpg"):
        print("image/jpg")
    
    elif media.endswith(".png"):
        print("image/png")
        
    elif media.endswith(".pdf"):
        print("application/pdf")
        
    elif media.endswith(".txt"):
        print("text/txt")
        
    elif media.endswith(".zip"):
        print("application/zip")
        
    elif media.endswith(".jpeg"):
        print("image/jpeg")
        
    else:
        print("application/octet-stream")
        
main()