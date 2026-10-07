#!/usr/bin/env python3
"""
def return_evens(num_list):
    even_list = []
    for i in num_list:
        if i % 2 == 0:
            even_list.append(i)
    
    return(even_list)

print(return_evens([0,1,2,3,4,5,6,7,8,9,10,11,12,13,13]))
"""

def return_evens(num_list):
    even_list = [i for i in num_list if i % 2 == 0]
    return(even_list)

print(return_evens([0,1,2,3,4,5,6,7,8,9,10,11,12,13,13]))



def make_exclamation(sentence_list):
    new_sentence = [i + "!" for i in sentence_list]
    
    return(new_sentence)

print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))







