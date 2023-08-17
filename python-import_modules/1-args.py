from argv import argv

if __name__ == "__main__":
    def print_arguments(argv):
        num_arguments = len(argv) - 1
        plural = 's' if num_arguments != 1 else ''
        print(f"{num_arguments} argument{plural}:")
    
        if num_arguments == 0:

            print()
        else:
                     
        
        # print()
            for i in range(1, len(argv)):
                print(f"{i}: {argv[i]}")
   
