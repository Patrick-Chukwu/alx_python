# from argv import argv

# if __name__ == "__main__":
#     length = len(argv)
    
#     if (length == 1):
#         print("1 argument:")
#         print("1: {}".format(argv))
    
    
        
#     elif (length > 1):
#         print("{} arguments:".format(length))
#         for index in range(len(argv)):
#             print("{}: {}".format(index, argv[index]))

#     else: 
#         print("0 arguments.")

import sys

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

if __name__ == "__main__":
    print_arguments(sys.argv)


