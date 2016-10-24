"""
Filename_rev: Finding Numbers in a Haystack.py

Author: Phillip Truong

Email Address: phil_t_@hotmail.com

Date: 2016-09-13

Summary of Requirements: (if applicable).  https://www.coursera.org/learn/python-network-data

Description: Counting numbers in lines and then adding them.

"""

import re

list_num = []

f = open('Finding Numbers in a Haystack (Actual)', 'r')

for line in f:
    line_num = (re.findall('[0-9]+', line))
    if line_num != []:
        for i in line_num:
            list_num.append(int(i))

print(sum(list_num))
