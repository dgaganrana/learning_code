#!/bin/python3

import re

# Defining method to search a word in string
#
def check_match(fun, word, string):
    mt = getattr(re,fun)(word,string)
    if mt:
        print('yes')
    else:
        print('no')

# This is the test string
#
st="hey what's yp 45 is the absence 70 and 1234 abba acc baac cca 1-4 - - - + + + * * * * }{ )( learn"
re_object_property = 'search'
search_word = 'learn'

# Here, calling method to search word in test string
# re_object_property: re method name
# search_word: test word to search in string
# st: test string
check_match(re_object_property, search_word, st)
