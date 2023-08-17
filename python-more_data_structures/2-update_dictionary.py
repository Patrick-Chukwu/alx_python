def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    keys = sorted(a_dictionary.keys())
    for key in a_dictionary:
        print("{}: {} ".format(key, a_dictionary[key]))
    
    print("xx")
    return a_dictionary


