from argv import argv

if __name__ == "__main__":
    length = len(argv)
    
    if (length == 1):
        print(1 argument:)
        print("1: {}".format(argv))
    
    
        
    elif (length > 1)
        print("{} arguments:".format(length))
        for (value in argv):
            print("{}: {}".format(indexof(value), value))

    else (length == 0):
        print("0 arguments.")

