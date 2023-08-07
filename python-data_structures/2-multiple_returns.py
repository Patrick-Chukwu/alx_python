def multiple_returns(sentence):
    if not sentence:
        first = None
    else :
        first = sentence[0]
    length = len(sentence)    
    print("Length: {:d} - First character: {}".format(length, first))
