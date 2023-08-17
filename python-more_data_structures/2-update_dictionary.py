def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    # keys = sorted(a_dictionary.keys())
    for key in a_dictionary:
        print("{}: {} ".format(key, a_dictionary[key]))
    
    print("xx")
    return
    # for key in a_dictionary:
    #     print("{}: {}".format(key, a_dictionary[key]))

    # return a_dictionary

# def print_sorted_dictionary(my_dict):
#     """ Print sorted dictionary """
#     keys = sorted(my_dict.keys())
#     for k in keys:
#         print("{}: {}".format(k, my_dict[k]))

# a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
# new_dict = update_dictionary(a_dictionary, 'language', "Python")
# print_sorted_dictionary(new_dict)
# print("--")
# print_sorted_dictionary(a_dictionary)


