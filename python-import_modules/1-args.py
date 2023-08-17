import sys

def print_arguments(argv):
    num_arguments = len(argv)
    if num_arguments == 0:
        print("0 arguments.")
    elif num_arguments == 1:
        print("1 argument:")
        print(f"1: {argv[0]}")
    else:
        print(f"{num_arguments} arguments:")
        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    print_arguments(sys.argv[1:])


# from argv import argv

# if __name__ == "__main__":
#     def print_arguments(argv):
#         num_arguments = len(argv) - 1
#         plural = 's' if num_arguments != 1 else ''
#         print(f"{num_arguments} argument{plural}:")
    
#         if num_arguments == 0:

#             print()
#         else:
                     
        
#         # print()
#             for i in range(1, len(argv)):
#                 print(f"{i}: {argv[i]}")
   
