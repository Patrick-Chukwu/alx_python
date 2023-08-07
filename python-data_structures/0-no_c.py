def no_c(my_string):

    result = []
    for character in my_string:
       if character != 'c' and character != 'C':
           result.append(character)
    return ''.join(result)

