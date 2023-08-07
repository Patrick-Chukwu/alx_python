def multiple_returns(sentence):
     
    if not sentence:
        return 0, None
    else :
        first = sentence[0]
    length = len(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
