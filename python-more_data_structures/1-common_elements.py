def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None:
        a_dictionary[key] = value

def print_sorted_dictionary(my_dict):
    if my_dict is not None:
        keys = sorted(my_dict.keys())
        for key in keys:
            print(f"{key}: {my_dict[key]}")