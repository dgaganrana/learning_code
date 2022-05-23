#!/bin/python3

# This program is to convert a nested list into one dimensional list
# Also using re module to split string

import re
from collections import Iterable

def one_dimensional_list(result):
  for element in result:
    if isinstance(element, Iterable) and not isinstance(element, str):
      for nested_element in one_dimensional_list(element):
        yield nested_element
    else:
      yield element

string = 'ten:12 fourty four:89:bread butter bun'
pattern_one = '\s'
pattern_two = ':'

result_one = re.split(pattern_one, string)
result_two = [re.split(pattern_two,word) for word in result_one]

plain_list = one_dimensional_list(result_two)
print(list(plain_list))
