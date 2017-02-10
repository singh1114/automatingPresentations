#!/usr/bin/env python

    # -*- coding: utf-8 -*-

"""
* MIT Licensed

* File Name : automatingScript.py

* Purpose : Creating Markdown presentations from powerpoint presentations

* Creation Date : 09-02-2017

* Copyright (c) 2017 Ranvir Singh <ranvir.singh1114@gmail.com>

"""

# Read the file:
#
#   whenever the line starts with *:
#
#     read each character:
#
#       if the letters are capital:
#         give heading h1
#
#       if the * is first in the group:
#         raise the height by 50%
#
#       if there is nothing after *
#         do nothing
#
#   if the line starts with References:
#     write the code for new slides

# open the given file in read mode
inputFile = open("FinInfSt.txt", "r")

# open another file where the changes are going to be made
outputFile = open("result.md", "w")

# temporary variable to check for the new slides
tempSlide = 1

# iterating over each line in the file
for line in inputFile:

    # spliting all the words in  the file
    words = line.split()
    # print words
    # print "\n"

    # iterating over all the words in a particular line
    for x in words:
        if(x == "References"):
            outputFile.write('\n---\n\n')
            tempSlide = 1

        if(x == "*"):
            if(tempSlide == 1):
                # Don't make a list
                # Set height = 150%
                tempSlide = 0
                continue

        if((x.isupper() and tempSlide == 0 and x != "*") or (x.isupper() and tempSlide == 2)):
            somestring1 = "# "
            newString = line
            newString = newString.replace('* ', '')

            allwords = newString.split()
            for y in allwords:
                if(y.isupper() or y.isdigit()):
                    newTemp = 1
                else:
                    newTemp = 0

            if(newTemp == 1):
                outputFile.write(somestring1 + newString + '\n')
                tempSlide = 2
                break

        elif(tempSlide == 0 and x != "*"):
            somestring1 = "### "
            newString = line
            newString = newString.replace('* ', '')
            outputFile.write(somestring1 + newString + '\n')
            tempSlide = 2
            break

        elif(tempSlide == 2 and x != "*"):
            somestring1 = "* "
            newString = line
            newString = newString.replace('* ', '')
            outputFile.write(somestring1 + newString + '\n')
            break

        #elif(tempSlide == 2):
