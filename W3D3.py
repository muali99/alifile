#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 28 18:53:34 2021

@author: ali
"""

file = open('my_file.txt', 'r')
numWords = file.read()
lines = numWords.split('\n')
words = numWords.split()
print('Number of lines:', len(lines))
print('Number of words:', len(words))

