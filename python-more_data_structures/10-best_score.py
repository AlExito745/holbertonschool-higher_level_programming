#!/usr/bin/python3
def best_score(a_dictionary):
    # return a key with the biggest integer value
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return(None)
    
    max_key = next(iter(a_dictionary))
    for key in a_dictionary:
        if a_dictionary[key] > a_dictionary[max_key]:
            max_key = key
    return(max_key)
