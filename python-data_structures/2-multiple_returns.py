# def multiple_returns(sentence):
     
#     if not sentence:
#         return 0, None
#     else :
#         first = sentence[0]
#     length = len(sentence)
#     print("Length: {:d} - First character: {}".format(length, first))


def multiple_returns(sentence):
    if not sentence:
        return 0, None  # Return 0 for length and None for first character
    else:
        first = sentence[0]
    
    length = len(sentence)
    return length, first