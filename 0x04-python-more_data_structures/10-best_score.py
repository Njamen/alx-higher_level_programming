#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        for key in a_dictionary:
            max = key
            break
        for key in a_dictionary:
            if a_dictionary[max] < a_dictionary[key]:
                max = key
        return max
    else:
        return None
