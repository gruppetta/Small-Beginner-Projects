'''
Interactive diary where the definition of words is provided , as well as a suggested word if the spelling is incorrect. 
'''

#Import json as standard library 

import json
import sys
from difflib import get_close_matches

#create dataset from json file (it is in the folder so no need to give directory)
data = json.load(open('dictionary.json'))


#lets see the type of data 
type(data)

#define function that gets definition 

def define(word):
    w = word.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches (w,data)) > 0:
        yn = input('The word is not in the dictionary. Did you mean.. %s' % get_close_matches(w, data.keys())[0])
        if yn == ('no' or 'No'):
            return 'ok no problem'
        elif yn == 'yes' or yn =='Yes':
            return data[get_close_matches(w,data)[0]]
        else:
            return 'The end' 
    else:
        return 'The word is not in the dictonary'


word = input('Enter word:  ')

output = define(word)

if type(output) == list:
    for a,item in enumerate(output):
        print(a,'.', item)
else:
    print(output)

