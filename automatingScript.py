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

# open another file where the changes are going to be made in write mode
outputFile = open("result.md", "w")

# temporary variable to check for the new slides
# About temporary variable tempSlide
# when tempSlide == "default",
#     -it means either
#               it is the first case
#               or 
#               the file pointer have encountered the word "References"
#
# when tempSlide == "headers",
#     -it means either
#               the file pointer have encountered a capital letter word
#               or
#               the file pointer have encountered the first element in the slide
#
# when tempSlide = "list",
#     -it means that
#               the list is going on.
tempSlide = "default"

oneMoreTemp = "default"

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
            tempSlide = "default"
            oneMoreTemp = "default"

        if(x == "*"):
            if(tempSlide == "default"):
                # Don't make a list
                # Set height = 150%
                tempSlide = "headers"

            else:
                oneMoreTemp = "default"

            continue

        if((x.isupper() and tempSlide == "headers" and x != "*") or (x.isupper() and tempSlide == "list")):
            somestring1 = "## "
            newString = line
            newString = newString.replace('* ', '')

            allwords = newString.split()

            # Checking that all the words are capitals
            for y in allwords:
                if(y.isupper() or y.isdigit()):
                    newTemp = 1
                else:
                    newTemp = 0

            if(newTemp == 1):
                outputFile.write(somestring1 + newString + '\n')
                tempSlide = "list"
                break

        elif(tempSlide == "headers" and x != "*"):
            somestring1 = "### "
            newString = line
            newString = newString.replace('* ', '')
            outputFile.write(somestring1 + newString + '\n')
            tempSlide = "list"
            break

        elif((tempSlide == "list" and x != "*") or oneMoreTemp == "continue"):
            if(oneMoreTemp == "continue"):
                somestring1 = ""
            else:
                somestring1 = "* "
            newString = line
            newString = newString.replace('* ', '')
            outputFile.write(somestring1 + newString)
            oneMoreTemp = "continue"
            break
